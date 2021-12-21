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
def user_option():
    option = input('''
Choose one of these options:
0. Exit
1. List all items #Done -Thu 
2. Search item by name #Done - Thu
3. Search item by item id #Done - Thu
4. List all information of a specific customer
5. Placing orders
6. Shipping management
7. Payment management
8. Discount
9. Return shipment 
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
            # exit
            if user == 0:
                cls()
                print('\nThank you for visiting our store! Hope to see you again!')
                exit(0)
            elif user == 1: # list items and get info of a specific item
                cls()
                list_all(product_field, json_data)
            elif user == 2: # search item by name 
                cls()
                search_by_name(product_field,json_data)
            elif user == 3: # search item by ID
                cls()
                search_item(product_field, json_data)
            elif user == 4: # Return shipment 
                cls()
                handle_order(json_data)
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
