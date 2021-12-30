import json
import string
import random
from components.styling import Style
from components.additional_features import discount

def handle_order(product_id, json_data):
    """
    The function handles product order event. 
    It updates product's quantity, 
    creates new order with order ID in database, 
    logs new customer data.

    :param: 
        product_id: product id that need to be handled (str)
        json_data: dictionary containing all data from database (dict)
    :return: None
    """
    updated_quantity = json_data['product'][product_id]['quantity']
    order_id = random_order_id(json_data)
    order_quantity = int(input("How many books would you like to get? "))
    updated_quantity -= order_quantity
    
    # Check if product's quantity is enough
    if updated_quantity < 0:
        print(f'\nWe only have {json_data["product"][product_id]["quantity"]} products left')
    else:
        # Generate customer and order dictionary
        customer_dict, order_dict, customer_id = handle_data(json_data, product_id, order_quantity)
                    
        # Write data to database
        json_data['customer'][customer_id] = customer_dict
        json_data['order'][order_id] = order_dict
        json_data['product'][product_id]['quantity'] = updated_quantity
        json_data['product'][product_id]['sold'] += order_quantity
        
        # create nested dictionary 
        for order_id in json_data['order']:
            for customer_id in json_data['customer']:
                order_field = json_data['order'][order_id]

                # copy order dictionary and remove customer_id, customer_address
                nested_order_dict = order_field.copy()
                remove_key = ['customer_id', 'customer_address', 'reviewed']
                for k in remove_key:
                    nested_order_dict.pop(k)

                # add new dictionary to the customer dictionary
                if json_data['order'][order_id]['customer_id'] == customer_id:
                    json_data["customer"][customer_id]["order"][order_id] = nested_order_dict

        json_file = open('data/data.json', 'w')
        json.dump(json_data, json_file, indent=4)
        print(f"\nYour order number is: {Style.BOLD}{order_id}{Style.END}\nPlease note for later use")


def random_order_id(json_data):
    """
    The function generates a random string of 7 characters consisting of uppercase letters and digits.
    Order ID generated is checked to make sure there is no duplicated ID.

    :param: 
        json_data: dictionary containing all data from database (dict)
    :return:
        random_id: 7 characters id (str)
    """
    # Modify 'k' for number of random_id character
    random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

    if json_data['order'] == {}:
        return random_id
    else:
        for i in json_data['order']:
            if i == random_id:
                return random_order_id(json_data)
            else:
                return random_id


def handle_data(json_data, product_id, order_quantity):
    """
    The function generates customer information dictionary and new order dictionary
    :param:
        json_data: dictionary containing all information (dict)
        product_id: product id of product being product (str)
        order_quantity: number of product bring bought (str)
    :return:
        customer_dict: new customer dictionary (dict)
        order_dict: new order dictionary (dict)
        customer_id: the customer id (str)
    """
    customer_field = json_data['customer']
    # Ask for customer ID or submit information 
    print("\n0. Not yet")
    print("1. Yes, and I have customer ID")
    purchase_history = input("Have you purchase from us ever before? ")
    
    # in case he/she has the customer ID
    if purchase_history == "1":
        try:    
            customer_id = input("Please submit your customer ID: ")
            customer_name = customer_field[customer_id]['name']
            customer_email = customer_field[customer_id]['email']
            customer_phone = customer_field[customer_id]['phone_num']
            customer_address = customer_field[customer_id]['address']

        except Exception as e:
            print(f'Customer id {e} does not exist, press any keys to try again')
            handle_order(product_id, json_data)

    # in case he/she does not have the customer ID
    elif purchase_history == "0":
        # customer_field's key is sorted in ascending order,
        # max id would be the last value from the json_data['customer'] list
        max_id = int(list(customer_field)[-1])
        customer_id = str(max_id + 1)  # Create new customer_id by add 1 to max id
        print("\n")
        customer_name = input("Name: ")
        customer_email = input("Email address: ")
        customer_phone = input("Phone number: ")
        customer_address = input("Shipping address: ")
        print(f'\nYour custumer ID is {Style.BOLD}{customer_id}{Style.END}')
    else:
        handle_order(product_id, json_data)

    discount_amount = discount(json_data, customer_id)
    total_price = int(order_quantity) * int(json_data["product"][product_id]["price"])
    final_price = total_price * (100 - discount_amount) * 0.01

    order_dict = {
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": int(order_quantity),
        "total_cost": final_price,
        "customer_address": customer_address,
        "reviewed": "False"
    }
    
    customer_dict = {
        "id": customer_id,
        "name": customer_name,
        "email": customer_email,
        "phone_num": customer_phone,
        "address": customer_address,
        "order": {}
    }

    # Display price
    print(f"You've got {discount_amount}% discount!")
    print(f'\nYour total cost is {final_price}$!')

    return customer_dict, order_dict, customer_id
