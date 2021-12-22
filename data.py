import json
from prettytable import PrettyTable

from handle_order import handle_order
from cls import cls
from styling import style

def list_all(json_data):
    '''
    The function print all products information from database.

    :param: dict: json_data: dictionary contain all data from database
    '''
    cls()
    try:
        table = PrettyTable(['ID', 'Book Title', 'Author', 'Description', 'Quantity', 'Price'])
        table.align = 'l'
        for item in json_data['product']:
            #print(f'{item}. {json_data["product"][item]["title"]}')
            table.add_row([
                item, 
                json_data['product'][item]['title'],
                json_data['product'][item]['author'],
                json_data['product'][item]['description'],
                json_data['product'][item]['quantity'],
                json_data['product'][item]['price'], ])
        print(table)
        get_item(json_data)
    except Exception as e:
        print(e)


def get_item(json_data):
    '''
    The function print out product's detailed description based on user's selection

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
                print( f'{style.BOLD}{detail:15}{style.END}: {json_data["product"][user_option][detail]}')

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
                list_all(json_data)
                break
            else:
                input('Invalid option, press any key to try again')
                cls()
                get_item(json_data)

        except Exception as e:
            print(e)
            print(
                f"The item {str(e)} does not exist! Please try a valid number!")
            get_item(json_data)
            break


def search_by_name(json_data):
    '''
    The function print out product's detailed description based ont its name/title

    :param: dict: json_data: dictionary contain all data from database
    '''
    product_exist = 0
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
                        product_exist += 1
                        for detail in json_data['product'][id]:
                            print( f'{style.BOLD}{detail:15}{style.END}: {json_data["product"][id][detail]}')

                        print("\n0. Exit to main menu")
                        print("1. Purchase")
                        product_option = input(
                            "Do you want to purchase this item? ")
                        if product_option == "1":
                            handle_order(id, json_data)
                            input(
                                "\nPress any key to go back to main menu: ")
                            break
                        elif product_option == "0":
                            cls()
                            break
                        else:
                            input('heh?')
                            print('Invalid option')
                if product_exist == 0:
                    print('Please try again: ')
                    search_by_name(json_data)
                cls()
                break

            except Exception as e:
                print(
                    f"The item {e} does not exist! Please try the valid name!")


def search_by_id(json_data):
    '''
    The function print out product's detailed description based on user's selection

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
                print( f'{style.BOLD}{detail:15}{style.END}: {json_data["product"][user_option][detail]}')

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
                break
            else:
                input('Invalid option, press any key to try again')
                cls()
                search_by_id(json_data)

        except Exception as e:
            print(e)
            print(
                f"The item {str(e)} does not exist! Please try a valid number!")
            search_by_id(json_data)
            break


def return_shipment(json_data):
    order_exist = 0
    cls()
    while True:
        order_id = input("Please input your order id: ")
        for i in json_data['order']:
            if i == order_id:
                order_exist += 1
                customer_name = input("What is the buyer's name? ")
                return_reason = input("What is your reason of return? ")
                json_data['return'][order_id] = {
                    "customer name": customer_name,
                    "reason of return": return_reason
                }
                json_file = open('data.json', 'w')
                json.dump(json_data, json_file, indent=4)
                print('\nSorry for your inconvinient.\nWe will process your request as soon as possible')
                input("Press any key to bo gack: ")
                
                cls()
                break
        if order_exist == 0:
            print('Order does not exist')
            print("\n 0. Exit")
            print("1. Try again")
            if input("Try again? ") == "1":
                return_shipment(json_data)
                break
        cls()
        break