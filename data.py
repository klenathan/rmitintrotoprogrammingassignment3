import platform
import os
import random
import string
import json


def cls():
    '''
    The function clear console/terminal based on the user's operating system
    '''
    if platform.system() == 'Windows':
        return os.system('cls')
    elif platform.system() == 'Darwin':
        return os.system('clear')
    elif platform.system() == 'Linux':
        return os.system('clear')
    else:
        return print("The program can only clear on Window, MacOS and Linux")


def list_all(json_data):
    '''
    The function print all products information from database.

    :param: dict: json_data: dictionary contain all data from database
    '''
    cls()
    try:
        for item in json_data['product']:
            print(f'{item}. {json_data["product"][item]["title"]}')
        search_item(json_data['product'], json_data)
    except Exception as e:
        print(e)


def search_item(json_data):
    '''
    The function print out product's detailed description based ont its id

    :param:
        dict: json_data: dictionary contain all data from database
    '''
    while True:
        user_option = input(
            "\nPlease enter the product ID to get all information of the item or press 0 to return to the main menu: ")
        if user_option == "0":
            cls()
            break
        try:
            cls()
            print('\n')
            for detail in json_data['product'][user_option]:
                print(
                    f'{detail:15}: {json_data["product"][user_option][detail]}')

            print("\n0. Exit to main menu")
            print("1. Purchase")
            product_option = input("Do you want to purchase this item? ")
            if product_option == "1":
                handle_order(user_option, json_data)
                exit_option = input(
                    "\nPress any key to go back to main menu: ")
                if exit_option:
                    cls()
                    break
                else:
                    break
            elif product_option == "0":
                cls()
                list_all(json_data['product'], json_data)
                break
        except Exception as e:
            print(e)
            print(
                f"The item {str(e)} does not exist! Please try a valid number!")
            search_item(json_data['product'], json_data)


def search_by_name(json_data):
    '''
    The function print out product's detailed description based ont its name/title

    :param: dict: json_data: dictionary contain all data from database
    '''
    while True:
        book_name = input(
            "\nPlease enter the book title or press 0 to return to the main menu: ")
        if book_name == "0":
            break
        else:
            try:
                for id in json_data['product']:
                    title = json_data['product'][id]["title"]
                    if title == book_name:
                        for detail in json_data['product'][id]:
                            print(
                                f'{detail:10}: {json_data["product"][id][detail]}')

                        print("\n0. Exit to main menu")
                        print("1. Purchase")
                        product_option = input(
                            "Do you want to purchase this item? ")
                        if product_option == "1":
                            handle_order(id, json_data)
                            exit_option = input(
                                "\nPress any key to go back to main menu: ")
                            if exit_option:
                                cls()
                                break
                            else:
                                break
                        elif product_option == "0":
                            cls()
                            list_all(json_data['product'], json_data)

            except Exception as e:
                print(
                    f"The item {e} does not exist! Please try the valid name!")


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
        customer_id = input("Please submit your customer ID: ")
        customer_name = customer_field[customer_id]['name']
        customer_email = customer_field[customer_id]['email']
        customer_phone = customer_field[customer_id]['phone_num']
        customer_address = customer_field[customer_id]['address']
    else:
        print("\n")
        customer_name = input("Name: ")
        customer_email = input("Email adress: ")
        customer_phone = input("Phone number: ")
        customer_address = input("Shipping address: ")

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
