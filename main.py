import json

from basic_features import list_all, search_item, search_by_name
from additional_features import return_shipment, handle_review, best_books
from cls import cls


def open_file():
    """
    The function opens the json file
    :param: None
    :return: data: dictionary containing all data from database (dict)
    """
    with open('data.json', 'r+', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


"""
Check-list:
0.  Exit
1.  List all items #Done -Thu 
2.  Search item by name #Done - Thu
3.  Search item by item id #Done - Thu
4.  List all information of a specific customer
5.  Placing orders #Done? Thai

6.  Payment management ## In Progress ### ??

7.  Discount # Done - Thu
8.  Return shipment # Done - Thai
9. Product review # Done - Thai
10. Top 5 best-selling books # Thu/Thinh ?
"""


def user_option():
    """
    The function takes the user input
    :param: None
    :return: 
        option: user option from 0 to 6 (int)
    """

    option = input('''
Choose one of these options:
0. Exit                     1. List all items
2. Search item by name      3. Search item by item id 
4. Return shipment          5. Review order product
6. Top 5 best-selling books
Your option:  ''')

    if option not in ['0', '1', '2', '3', '4', '5', '6']:
        cls()
        print('Wrong input, please try again!')
        option = '-1'
    return int(option)


if __name__ == '__main__':
    try:
        while True:
            user = user_option()
            json_data = open_file()
            # Exit program
            match user:
                case 0:
                    cls()
                    print('\nThank you for visiting our store! Hope to see you again!')
                    exit(0)
                # List items and get info of a specific item
                case 1:
                    cls()
                    list_all(json_data)
                # Search item by name
                case 2:
                    cls()
                    search_by_name(json_data)
                # Search item by ID
                case 3:
                    cls()
                    search_item(json_data)
                # Return shipment
                case 4:
                    cls()
                    return_shipment(json_data)
                # Review
                case 5: 
                    cls()
                    handle_review(json_data)
                # Best-selling books
                case 6:
                    cls()
                    best_books(json_data)
    except KeyboardInterrupt:
        cls()
