import json

from data import list_all, search_item, search_by_name
from additional_features import return_shipment, handle_review
from cls import cls

# Open file json
def open_file():
    with open('data.json', 'r+') as json_file:
        json_data = json.load(json_file)
        return json_data

"""
Check-list:
0.  Exit
1.  List all items #Done -Thu 
2.  Search item by name #Done - Thu
3.  Search item by item id #Done - Thu
4.  List all information of a specific customer ???
5.  Placing orders | To-do: a lot ...| #Done? Thai

7.  Payment management ## In Progress ### ??

8.  Discount # Done - Thu
9.  Return shipment # Done - Thai
10. Product review # Done - Thai
11. Used product 70% price 
"""
# User option
def user_option():
    option = input('''
Choose one of these options:
0. Exit                     1. List all items
2. Search item by name      3. Search item by item id 
4. Return shipment          5. Review order product
Your option:  ''')
    if(option not in ['0', '1', '2', '3', '4', '5']):
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
            if user == 0:
                cls()
                print('\nThank you for visiting our store! Hope to see you again!')
                exit(0)
            # List items and get info of a specific item
            elif user == 1:
                cls()
                list_all(json_data)
            # Search item by name
            elif user == 2:
                cls()
                search_by_name(json_data)
            # Search item by ID
            elif user == 3:
                cls()
                search_item(json_data)
            # Return shipment
            elif user == 4:
                cls()
                return_shipment(json_data)
            # Review
            elif user == 5: 
                cls()
                handle_review(json_data)

    except KeyboardInterrupt:
        cls()
