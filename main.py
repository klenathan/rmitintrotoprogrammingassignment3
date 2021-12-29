import json
from components.basic_features import list_all, search_item, search_by_name, purchase_tracking
from components.additional_features import return_shipment, handle_review, best_books
from components.cls import cls
from components.logo import welcome, bye


def open_file():
    """
    The function opens the json file
    :param: None
    :return: data: dictionary containing all data from database (dict)
    """
    with open('data/data.json', 'r+', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def user_option():
    """
    The function takes the user input
    :param: None
    :return: 
        option: user option from 0 to 6 (int)
    """
    print(welcome)

    option = input('''
Choose one of these options:
0. Exit
                   
1. List all items               2. Search item by name
3. Search item by item id       4. Customer information & purchase history

5. Return shipment              6. Review order product
7. Best-selling books rank     
Your option:  ''')

    if option not in ['0', '1', '2', '3', '4', '5', '6', '7']:
        cls()
        print('Wrong input, please try again!')
        option = '-1'
    return int(option)


if __name__ == '__main__':
    try:
        while True:
            user = user_option()
            json_data = open_file()
            match user:
                # Exit program
                case 0:
                    cls()
                    print(bye)
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
                # Track purchase history
                case 4:
                    cls()
                    purchase_tracking(json_data)
                # Return shipment
                case 5:
                    cls()
                    return_shipment(json_data)
                # Review
                case 6:
                    cls()
                    handle_review(json_data)
                # Best-selling books
                case 7:
                    cls()
                    best_books(json_data)
                

    except KeyboardInterrupt:
        cls()
