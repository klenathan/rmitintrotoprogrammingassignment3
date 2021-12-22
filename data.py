import json
from prettytable import PrettyTable

from handle_order import handle_order
from cls import cls

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
        search_item(json_data)
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
                print(f'{detail:15}: {json_data["product"][user_option][detail]}')

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
                search_item(json_data)

        except Exception as e:
            print(e)
            print(
                f"The item {str(e)} does not exist! Please try a valid number!")
            search_item(json_data)


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
                            list_all(json_data)
                        else:
                            input('heh?')
                            print('Invalid option')

            except Exception as e:
                print(
                    f"The item {e} does not exist! Please try the valid name!")


def return_shipment(json_data):
    cls()
    while True:
        order_id = input("Please input your order id: ")
        for i in json_data['order']:
            if i == order_id:
                customer_name = input("What is the buyer's name? ")
                return_reason = input("What is your reason of return? ")
                json_data['return'][order_id] = {
                    "customer name": customer_name,
                    "reason of return": return_reason
                }
                print('\nSorry for your inconvinient.\nWe will process your request as soon as possible')
                input("Press any key to bo gack: ")
                cls()
                break
            else:
                print('Order does not exist')
                print("\n 0. Exit")
                print("\n 1. Try again")
                if input("Try again? ") == "1":
                    return_shipment(json_data)
                    break
                cls()
        break