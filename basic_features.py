from prettytable import PrettyTable
from handle_order import handle_order
from cls import cls
from styling import Style


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
            table = PrettyTable(
                ['ID', 'Book Title', 'Author', 'Quantity', 'Price', "Rating"])
            table.align = 'l'
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
        if user_option == "0":
            cls()
            return "0"
        else:
            try:
                product_option = query_detail(json_data, user_option)

                if product_option == "1":
                    handle_order(user_option, json_data)
                    input("\nPress any key to exit: ")
                    cls()
                    break
                elif product_option == "0":
                    cls()
                    break
                else:
                    input('Invalid option, press any key to try again ')
                    cls()
                    search_item(json_data)
                    break

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
    while True:
        book_name = input(
            "\nPlease enter the book title or press 0 to return to the main menu: ")
        if book_name == "0":
            break
        else:
            try:
                for product_id in json_data['product']:
                    title = json_data['product'][product_id]["title"]
                    if title == book_name:
                        product_exist += 1
                        for detail in json_data['product'][product_id]:
                            if detail == "rating":
                                print(
                                    f'{Style.BOLD}{detail:15}{Style.END}: '
                                    f'{json_data["product"][product_id][detail]["average"]:.2f}')
                            else:
                                print(
                                    f'{Style.BOLD}{detail:15}{Style.END}: '
                                    f'{json_data["product"][product_id][detail]}')
                        print("\n0. Exit")
                        print("1. Purchase")
                        product_option = input(
                            "Do you want to purchase this item? ")
                        if product_option == "1":
                            handle_order(product_id, json_data)
                            input(
                                "\nPress any key to go back to main menu: ")
                            break
                        elif product_option == "0":
                            cls()
                            break
                        else:
                            input('Invalid option, press any key: ')
                            break
                if product_exist == 0:
                    print('Please try again: ')
                    search_by_name(json_data)
                cls()
                break

            except Exception as e:
                print(
                    f"The item {e} does not exist! Please try the valid name!")


def query_detail(json_data, user_option):
    '''
    The function print out details of specific product and return
    user's option to purchase the item or not in string of "0" or "1"
    :param:
        json_data: dictionary containing all data from database (dict)
        user_option: product ID needed to be query (str)
    :return:
        product_option: user's option to purchase (str)
    '''
    cls()
    print('\n')
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

    print("\n0. Exit")
    print("1. Purchase")
    product_option = input("Do you want to purchase this item? ")
    return product_option


def purchase_tracking(json_data):
    while True:
        user_option = input(
            "\nPlease enter your ID to view the purchase history or press 0 to exit: ")
        try:
            if int(user_option) == 0:
                cls()
                break
            else:
                for detail in json_data['customer'][user_option]:
                    if detail == "order":
                        print(f"{Style.BOLD}order list{Style.END}:")
                        for order_id in json_data['customer'][user_option]["order"]:
                            print('\n')
                            print(f'{Style.BLUE}{order_id:12}{Style.END}')
                            for order_detail in json_data['customer'][user_option]['order'][order_id]:
                                print(
                                    f'{Style.BOLD}{order_detail:12}{Style.END}: {json_data["customer"][user_option]["order"][order_id][order_detail]}')                    
                    else:
                        print(
                            f'{Style.BOLD}{detail:12}{Style.END}: {json_data["customer"][user_option][detail]}')

        except Exception as e:
            print(f'Customer id {e} does not exist')
