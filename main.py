from data import *
import json


# open file json
def open_file():
    with open('data.json', 'r+') as json_file:
        json_data = json.load(json_file)
        product_field = json_data['product']
        customer_field = json_data['customer']
        return json_data, product_field, customer_field, json_file


# user option

"""
Check-list:
0. Exit
1. List all items #Done -Thu 
2. Search item by name #Done - Thu
3. Search item by item id #Done - Thu
4. List all information of a specific customer
5. Placing orders #Done? Thai To-do: implement 4 to 5
6. Shipping management
7. Payment management
8. Discount
9. Return shipment -> should have ?
"""

def user_option():
    option = input('''
Choose one of these options:
0. Exit                     1. List all items
2. Search item by name      3. Search item by item id 
4. Return shipment
Your option:  ''')
    if(option not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
        print('Wrong input, please try again!')
        option = '-1'
    return int(option)


if __name__ == '__main__':
    try:
        while True:
            user = user_option()
            json_data, product_field, customer_field, json_file = open_file()
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
            elif user == 4:
                cls()
                return_shipment(json_data)
            elif user == 5:
                cls()
                pass
            elif user == 6:
                cls()
                pass
            elif user == 7:
                cls()
                pass
            elif user == 8:
                cls()
                pass
            elif user == 9:
                cls()
                pass

    except KeyboardInterrupt:
        cls()
