import json
import string
import random
from cls import cls
from styling import style


def handle_order(product_id, json_data):
    '''
    The function handle product order event. 
    It updates product's quantity, 
    create new order with order ID in database, 
    log new customer data.

    :param: 
        str: product_id: product id that need to be handle
        dict: json_data: dictionary contain all data from database
    '''

    order_id = random_order_id(json_data)
    order_quantity = input("How many would you like to get? ")
    updated_quantity = json_data['product'][product_id]['quantity'] - int(order_quantity)

    # Check if product's quantity is enough
    if updated_quantity < 0:
        print(f'\nWe only have {json_data["product"][product_id]["quantity"]} products left')
    else:
        # Generate customer and order dictionary
        customer_dict, order_dict, customer_id = handle_customer_info(json_data, product_id, order_id, order_quantity)
        # Review
        rating_dict = handle_review(json_data, product_id)
        # Write data to database
        json_data['customer'][customer_id] = customer_dict
        json_data['order'][order_id] = order_dict
        json_data['product'][product_id]['quantity'] = updated_quantity
        json_data['product'][product_id]['rating'] = rating_dict
        json_file = open('data.json', 'w')

        json.dump(json_data, json_file, indent=4)

        print(
            f"\nYour order number is: {style.BOLD}{order_id}{style.END}\nPlease note for later use")


def random_order_id(json_data):
    '''
    The function generate a random string of 7 characters consist of uppercase letters and digits.
    Order ID generated is check to make sure there is no duplicated ID.

    :param: 
        str: product_id: product id that need to be handle
        dict: json_data: dictionary contain all data from database
    :return:
        str: random_id: 7 characters id 
    '''
    random_id = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=7)
    ) # Modify 'k' for number of random_id character 

    if json_data['order'] == {}:
        return random_id
    else:
        for i in json_data['order']:
            if i == random_id:
                return random_order_id(json_data)
            else:
                return random_id

def handle_customer_info(json_data, product_id, order_id, order_quantity):
    '''
    The function generate customer information dictionary and new order dictinary
    :param:
        dict: json_data: dictionary contain all information
        str: product_id: product id of product being product
        str: order_id: order id that need to be generate
        str: order_quantity: number of product bring bought
    :return:
        dict: customer_dict: new customer dictionary
        dict: order_dict: new order dictionary
    '''
    customer_field = json_data['customer']
    # Ask for customer ID or submit information 
    print("\n0. Not yet")
    print("1. Yes, and I have customer ID")
    purchase_history = input("Have you purchase from us ever before? ")
    if purchase_history == "1":
        try:    
            customer_id = input("Please submit your customer ID: ")
            customer_name = customer_field[customer_id]['name']
            customer_email = customer_field[customer_id]['email']
            customer_phone = customer_field[customer_id]['phone_num']
            customer_address = customer_field[customer_id]['address']
        except Exception as e:
            print(f'Customer id {e} does not exist, press anykey to try again')
            handle_order(product_id, json_data)
    elif purchase_history == "0":
        # customer_field's key is sorted ascendingly, 
        # max id would be the last value from the json_data['customer'] list
        max_id = int(list(customer_field)[-1])
        customer_id = str(max_id + 1) # Create new customer_id by add 1 to max id
        print("\n")
        customer_name = input("Name: ")
        customer_email = input("Email adress: ")
        customer_phone = input("Phone number: ")
        customer_address = input("Shipping address: ")
    else:
        handle_order(product_id, json_data)
    customer_dict = {
        "id": customer_id,
        "name": customer_name,
        "email": customer_email,
        "phone_num": customer_phone,
        "address": customer_address
    }
    order_dict = {
        "id": order_id,
        "customer_id": customer_id,
        "product_id": product_id,
        "buy_quantity": int(order_quantity),
        "customer_address": customer_address
    }
    total_price = int(order_quantity) * int(json_data["product"][product_id]["price"])
    #final_price = total_price * (100 - discount(json_data))
    #Display price
    print(f'\nTotal cost is: {total_price}$')

    return customer_dict, order_dict, customer_id

def handle_review(json_data, product_id):
    total_point = json_data["product"][product_id]["rating"]["total_point"]
    num_of_review = json_data["product"][product_id]["rating"]["num_of_review"]
    
    user_review = int(input("\nHow do you rate the product from 1 to 5? "))
    if user_review > 5:
        user_review == 5
    elif user_review < 1:
        user_review == 1
    
    total_point += user_review
    num_of_review += 1
    average_point = total_point/num_of_review

    rating_dict = {
        "total_point": total_point,
        "num_of_review": num_of_review,
        "average": average_point
    }

    return rating_dict

def discount(json_data, product_id): ############ TO DO
    customer_id_input = input('Please enter your customer id: ')
    total_items = 0
    total_cost = 0
    for order_id in json_data['order']:
        customer_id = json_data['order'][order_id]['customer_id']
        if customer_id_input == customer_id:
            total_items = int(json_data['order'][order_id]['quantity'])
            total_cost = total_items * json_data["product"][product_id]

    if total_items >= 10:
        discount = 10
    elif total_items >= 5:
        discount = 5
    elif total_items >= 3:
        discount = 3
    total_cost = total_cost * (100-discount)/100    

    print(f"You've got {discount}% discount! Your total cost is {total_cost}!")
