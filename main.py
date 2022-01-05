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


import json
from components.basic_features import list_all, search_item, search_by_name, purchase_tracking
from components.additional_features import return_shipment, handle_review, best_books
from components.cls import cls
from components.logo import welcome, bye
from components.faq import faq

### note
'''
Video content           
1. List all items # Thai          
2. Search item by item id # Thai

3. Search item by name # Thu
4. Customer information & purchase history #Thu

5. Return shipment # Thinh     
6. Best-selling books rank #Thinh      

7. Review order product # Soohyuk
8. Customer Service (FAQ) # Soohyuk
Your option:  '''


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
                   
1. List all items               2. Search item by item id
3. Search item by name          4. Customer information & purchase history

5. Return shipment              6. Best-selling books rank
7. Review order product         8. Customer Service (FAQ)
Your option:  ''')

    if option not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
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
                print(bye)
                exit(0)
            # List items and get info of a specific item
            elif user == 1:
                cls()
                list_all(json_data)
            # Search item by ID
            elif user == 2:
                cls()
                search_item(json_data)
            # Search item by name
            elif user == 3:
                cls()
                search_by_name(json_data)
            # Track purchase history
            elif user == 4:
                cls()
                purchase_tracking(json_data)
            # Return shipment
            elif user == 5:
                cls()
                return_shipment(json_data)
            # Best-selling books
            elif user == 6:
                cls()
                best_books(json_data)
            # Review
            elif user == 7:
                cls()
                handle_review(json_data)
            # Customer Service (FAQ)
            elif user == 8:
                cls()
                faq()
    except KeyboardInterrupt:
        cls()
