import json
import os
from book import *
from basic_features import *

with open('data.json') as json_file:
    json_data = json.load(json_file)
    product_field = json_data['product']


def cls(): 
    return os.system('cls')

# Main menu
def main_menu():
    options = {
        "1": "List all items",
        "2": "Search product by name",
        "3": "Search product by id",
        "4": "List all customers",
        "5": "To-do: Place Order",
        "\n0": "End program"
    }
    cls()
    for opt in options:
        print(f'{opt}: {options[opt]}')

    user_option = input("Please choose: ")

    if user_option == "0":
        exit()
    elif user_option == "1":
        list_all()
    elif user_option == "2":
        search_name(json_data)
    elif int(user_option) > 5:
        cls()
        print("Feature not yet implemented")
        print('\n0: Exit')
        go_back_to_main()
    else:
        cls()
        print("Unknown Error")
        print("Feature not yet implemented")
        print('\n0: Exit')
        go_back_to_main()

# Menu components


def search_name(data):
    '''
    This function render search by name menu
    :param: dict: data from json file contain all infomation
    '''
    searched_book_id = search_by_name(data)
    cls()
    if searched_book_id == None:
        print('Book not found')
    else:
        for detail in product_field[searched_book_id]:
            print(f'{detail}: {product_field[searched_book_id][detail]}')

    print('\n0: Exit')
    user_option = input("\nPlease choose: ")
    if user_option == "0":
        main_menu()


def list_all():
    '''
    This function render product information
    '''
    cls()
    for item in product_field:
        print(f'{item}: {product_field[item]["title"]}')
    print('\n0: Exit')
    user_option = input("\nPlease choose: ")
    if user_option == "0":
        main_menu()
    else:
        cls()
        for detail in product_field[user_option]:
            print(f'{detail}: {product_field[user_option][detail]}')
        print('\n0: Go Back')
        user_option_2 = input("\nPlease choose: ")
        if user_option_2 == "0":
            cls()
            for item in product_field:
                print(f'{item}: {product_field[item]["title"]}')
            print('\n0: Exit')
            user_option = input("\nPlease choose: ")


def go_back_to_main():
    user_option = input("\nPlease choose: ")
    if user_option == "0":
        main_menu()


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        cls()
