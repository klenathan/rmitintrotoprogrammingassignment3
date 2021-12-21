import json
import os
import platform
from book import *
from basic_features import *

with open('data.json') as json_file:
    json_data = json.load(json_file)
    product_field = json_data['product']


def cls(): 
    if platform.system() == 'Windows':
        return os.system('cls')
    elif platform.system() == 'Darwin':
        return os.system('clear')
    elif platform.system() == 'Linux':
        return os.system('clear')
    else:
        return print("The program can only clear on Window, MacOS and Linux")
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
    elif user_option == "3":
        search_id(json_data)
    elif user_option == "4":
        list_all_customer()
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


def list_all(data):
    '''
    This function render product information
    '''
    cls()
    for item in data['product']:
        print(f'{item}: {data["product"][item]["title"]}')
    print('\n0: Exit')
    user_option = input("\nPlease choose: ")
    if user_option == "0":
        main_menu()
    else:
        cls()
        for detail in data['product'][user_option]:
            print(f'{detail}: {data["product"][user_option][detail]}')
        print('\n0: Go Back')
        user_option_2 = input("\nPlease choose: ")
        if user_option_2 == "0":
            cls()
            list_all()
            user_option = input("\nPlease choose: ")
            if user_option == 0:
                print('ej')
                main_menu()

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
        for detail in data['product'][searched_book_id]:
            print(f'{detail}: {data["product"][searched_book_id][detail]}')

    print('\n0: Exit')
    user_option = input("\nPlease choose: ")
    if user_option == "0":
        main_menu()

def search_id(data):
    '''
    This function render search by id menu
    :param: dict: data from json file contain all infomation
    '''
    searched_book_data = search_by_id(data)
    cls()
    if searched_book_data == None:
        print('Book not found')
    else:
        for detail in searched_book_data:
            print(f'{detail}: {searched_book_data[detail]}')

    print('\n0: Exit')
    user_option = input("\nPlease choose: ")
    if user_option == "0":
        main_menu()


def list_all_customer(data):
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
            list_all()
            user_option = input("\nPlease choose: ")
            if user_option == 0:
                print('ej')
                main_menu()

def go_back_to_main():
    user_option = input("\nPlease choose: ")
    if user_option == "0":
        main_menu()


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        cls()
