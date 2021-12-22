import json
import string
import random
from cls import cls


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
    customer_field = json_data['customer']
    # customer_field's key is sorted ascendingly
    max_id = int(list(customer_field)[-1])
    customer_id = str(max_id + 1)
    customer_address = ''
    order_id = random_order_id(json_data)

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
        print("\n")
        customer_name = input("Name: ")
        customer_email = input("Email adress: ")
        customer_phone = input("Phone number: ")
        customer_address = input("Shipping address: ")
    else:
        handle_order(product_id, json_data)

    cls()

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
        "customer_address": customer_address
    }
    json_data['product'][product_id]['quantity'] -= 1
    json_data['customer'][customer_id] = customer_dict
    json_data['order'][order_id] = order_dict
    json_file = open('data.json', 'w')

    json.dump(json_data, json_file, indent=4)

    print(
        f"\nYour order number is: \033[1m{order_id}\033[0m \nPlease note for later use")


def random_order_id(json_data):
    '''
    The function generate a random string of 7 characters consist of uppercase letters and digits.
    Order ID generated is check to make sure there is no duplicated ID.

    :param: 
        str: product_id: product id that need to be handle
        dict: json_data: dictionary contain all data from database
    :return:
        str: random_id: 7 characters order id 
    '''
    random_id = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=7)) # Modify k for number of random_id character 
    if json_data['order'] == {}:
        return random_id
    else:
        for i in json_data['order']:
            if i == random_id:
                return random_order_id(json_data)
            else:
                return random_id