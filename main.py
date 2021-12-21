import json
from book import *
from basic_features import *

def open_file():
    with open('data.json') as json_file:
        json_data = json.load(json_file)
        product_field = json_data['product']
        return json_data, product_field


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

    while True:
        print('\n')
        for opt in options:
            print(f'{opt}: {options[opt]}')
        user_option = input("Please choose a valid option as above: ")
        json_data, product_field = open_file()
        if user_option not in ['0', '1', '2', '3', '4', '5']:
            print('Invalid command! Please try again!')
            continue
        if user_option == "0":
            exit(0)
        elif user_option == "1":
            list_all(product_field)
        elif user_option == "2":
            search_name(json_data, product_field)
        elif user_option == "3":
            get_specific_item(product_field)  

# Menu components


def search_name(data, product_field):
    '''
    This function render search by name menu
    :param: dict: data from json file contain all infomation
    '''
    book_name = input("Please enter the book title: ")
    searched_book_id = search_by_name(data, book_name)
    if searched_book_id == None:
        search_name(data, product_field)
    else:
        print('\n')
        for detail in product_field[searched_book_id]:
            print(f'{detail}: {product_field[searched_book_id][detail]}')


def list_all(product_field):
    '''
    This function render product information
    '''
    print('\n')
    try:
        for item in product_field:
            print(f'{item}: {product_field[item]["title"]}')
   
    except Exception as e:
        print(e)


def get_specific_item(product_field):
    user_option = input("\nPlease choose a specific item or 0 to go back to main menu: ")
    if user_option == "0":
        main_menu()
    try:
        print('\n')
        for detail in product_field[user_option]:
            print(f'{detail}: {product_field[user_option][detail]}')
        list_all(product_field)
    except Exception as e:
        print(f"The item {e} does not exist! Please try a valid number!")
        get_specific_item(product_field)


def go_back_to_main():
    user_option = input("\nPlease choose: ")
    if user_option == "0":
        main_menu()


if __name__ == '__main__':
    try:
        main_menu()
    except Exception as e:
        print(e)
