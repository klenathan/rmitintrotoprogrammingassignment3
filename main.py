from data import list_all, search_by_name, search_item
import json

# open file json 
def open_file():
    with open('data.json') as json_file:
        json_data = json.load(json_file)
        product_field = json_data['product']
        return json_data, product_field


# user option
def user_option():
    option = input('''
Choose one of these options:
0. Exit
1. List all items
2. Search item by name
3. Search item by item id
4. List all information of a specific customer
5. Placing orders
6. Shipping management
7. Payment management
8. Discount
9. Return shipment # qua data.py di
Your option:  ''')
    if(option not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
        print('Wrong input, please try again!')
        option = '-1'
    return int(option)


if __name__ == '__main__':
    try:
        while True:
            user = user_option()
            json_data, product_field = open_file()
            # exit
            if user == 0:
                print('Thank you for visiting our store! Hope to see you again!')
                exit(0)
            # list items and get info of a specific item
            elif user == 1:
                list_all(product_field)
            # search item by name
            elif user == 2:
                search_by_name()
            # search item by ID
            elif user == 3:
                search_item()
            elif user == 4:
                pass
            elif user == 5:
                pass
            elif user == 6:
                pass
            elif user == 7:
                pass
            elif user == 8:
                pass
            elif user == 9:
                pass

    except Exception:
        print("Invalid input!!! Please try to enter another option in the list!")


