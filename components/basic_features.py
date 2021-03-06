# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 3
# Author:
#         Thai Tran (s3891890)
#         Thu Pham (s3878246)
#         Thinh Nguyen (s3914412)
#         Soohyuk Jang (s3928379)
# Created date: 20/12/2021
# Last modified date: 05/01/2022
# Python version: 3.10.0


from prettytable import PrettyTable
from components.handle_order import handle_order
from components.cls import cls
from components.styling import Style


def list_all(json_data):
    """
    The function prints all products information from database.
    :param: 
        json_data: dictionary contain all data from database (dict)
    :return: None
    """
    cls()
    while True:
        try:
            # create a table containing all product information
            table = PrettyTable(
                ['ID', 'Book Title', 'Author', 'Quantity', 'Price', "Rating"])
            table.align = 'l'

            # loop through product dictionary to add information to the table
            for item in json_data['product']:
                table.add_row([
                    item,
                    json_data['product'][item]['title'],
                    json_data['product'][item]['author'],
                    json_data['product'][item]['quantity'],
                    json_data['product'][item]['price'],
                    f'{json_data["product"][item]["rating"]["average"]:.2f}'
                ])
            print(table)

            # return to the main menu
            if search_item(json_data) == "0":
                break

        except Exception as e:
            print(e)


def search_item(json_data):
    """
    The function prints out product's detailed description based on product id
    :param:
        json_data: dictionary containing all data from database (dict)
    :return: None
    """
    while True:
        user_option = input(
            "\nPlease enter the product ID to get all information of the item or press 0 to exit: ")

        # return to the main menu if user input is "0"
        if user_option == "0":
            cls()
            return "0"
        # in other case
        else:
            # check whether the item exists or not
            try:
                purchase(json_data, user_option)

            except Exception as e:
                print(e)
                print(
                    f"The item {str(e)} does not exist! Please try a valid number!")


def search_by_name(json_data):
    """
    The function prints out product's detailed description based ont its name/title
    :param: json_data: dictionary containing all data from database (dict)
    :return: None
    """
    product_exist = 0
    search_result = []
    while True:
        book_name = input(
            "\nPlease enter the book title or press 0 to return to the main menu: ")

        # return to the main menu if user input is "0"
        if book_name == "0":
            cls()
            break
        # check for case sensitivity
        elif book_name == "" or book_name == " ":
            input("\nInvalid name, press any key to try again ")
        # in other case
        else:
            # loop through the product dictionary
            # to check whether the item exists or not
            for product_id in json_data['product']:
                title = json_data['product'][product_id]["title"]

                # in case the user input is valid
                if book_name.lower().replace(' ', '') in title.lower().replace(' ', ''):

                    product_exist = 1
                    search_result.append(product_id)

            # Print search result
            if product_exist == 0:
                input("Product not found\nPress any key to try again ")
            else:
                table = PrettyTable(
                    ['ID', 'Book Title', 'Author', 'Quantity', 'Price', "Rating"])
                table.align = 'l'

                # loop through product dictionary to add information to the table
                for item in search_result:
                    table.add_row([
                        item,
                        json_data['product'][item]['title'],
                        json_data['product'][item]['author'],
                        json_data['product'][item]['quantity'],
                        json_data['product'][item]['price'],
                        f'{json_data["product"][item]["rating"]["average"]:.2f}'
                    ])
                print(table)
                # Get user input
                user_opt = input(
                    "Choose by product id or press 0 to go back to main menu ")
                try:
                    # If user chose "0"
                    if user_opt == "0":
                        cls()
                        break
                    # in case user input the product id in the table
                    elif user_opt in search_result:
                        purchase(json_data, user_opt)
                        break
                    else: 
                        print("Please enter the product ID in the table")
                        search_by_name(json_data)
                # Print Error
                except Exception as e:
                    print(f'{e} does not exist')
                break


def purchase(json_data, user_opt):
    """
    The function prints out product's detailed description based ont its name/title
    :param: json_data: dictionary containing all data from database (dict)
            user_opt: the user option (str)
    :return: None
    """
    while True:
        product_option = query_detail(json_data, user_opt)

        # in case they want to purchase the item
        if product_option == "1":
            handle_order(user_opt, json_data)
            input("\nPress any key to exit: ")
            cls()
            break
        # in case they do not want to purchase the item
        elif product_option == "0":
            cls()
            break
        # in case their input is invalid
        else:
            input('Invalid option, press any key to try again ')
            cls()


def query_detail(json_data, user_option):
    """
    The function prints out details of specific product and return
    user's option to purchase the item or not in string of "0" or "1"
    :param:
        json_data: dictionary containing all data from database (dict)
        user_option: product ID needed to be queried (str)
    :return:
        product_option: user's option to purchase (str)
    """
    cls()
    print('\n')
    print(
        f'{Style.BOLD}{"product_id":12}{Style.END}: {user_option}')
    # loop through the product dictionary that matches the user input to print out all product information
    for detail in json_data['product'][user_option]:
        if detail == "rating":
            print(
                f'{Style.BOLD}{detail:12}{Style.END}: {json_data["product"][user_option][detail]["average"]:.2f}')
        elif detail == "description":
            print(
                f'{Style.BOLD}{detail:12}{Style.END}:\n{json_data["product"][user_option]["description"][:]}')
        else:
            print(
                f'{Style.BOLD}{detail:12}{Style.END}: {json_data["product"][user_option][detail]}')

    # ask whether they want to purchase this item
    print("\n0. Exit")
    print("1. Purchase")
    product_option = input("Do you want to purchase this item? ")

    return product_option


def purchase_tracking(json_data):
    """
    The function prints out all information of a specific customer, 
    including their purchase history
    :param:
        json_data: dictionary containing all data from database (dict)
    :return: None
    """
    while True:
        user_option = input(
            "\nPlease enter your ID to view the purchase history or press 0 to exit: ")

        # return to the main menu if the user input is '0'
        if user_option == '0':
            cls()
            break
        # in other case
        else:
            try:
                # loop through the customer dictionary that matches user input to print out all customer information
                for detail in json_data['customer'][user_option]:

                    if detail == "order":
                        print(f"\n{Style.BOLD}order list{Style.END}:")

                        # loop through the nested order dictionary
                        for order_id in json_data['customer'][user_option]["order"]:
                            print(
                                f'\n{Style.BLUE}{order_id:12}{Style.END}')

                            # loop through the nested order dictionary to print out all order information
                            for order_detail in json_data['customer'][user_option]['order'][order_id]:
                                print(
                                    f'{Style.BOLD}{order_detail:12}{Style.END}: '
                                    f'{json_data["customer"][user_option]["order"][order_id][order_detail]}')

                    else:
                        print(
                            f'{Style.BOLD}{detail:12}{Style.END}: {json_data["customer"][user_option][detail]}')

            except Exception as e:
                print(f'Customer id {e} does not exist')
