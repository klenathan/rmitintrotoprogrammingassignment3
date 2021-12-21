def list_all(product_field):
    '''
    This function render product information
    '''
    print('\n')
    try:
        for item in product_field:
            print(f'{item}. {product_field[item]["title"]}')
        search_item(product_field)
    except Exception as e:
        print(e)
#  


def search_item(product_field):
    while True:
        user_option = input("\nPlease choose a valid number to get all the information of the item or press 0 to return to the main menu: ")
        if user_option == "0":
            break
        try:
            print('\n')
            for detail in product_field[user_option]:
                print(f'{detail}: {product_field[user_option][detail]}')  

            # Return to list of items
            user_option = input("\nPress 0 to go back to the list of items: ")
            if user_option == 0:
                list_all(product_field) 
            
                    # 
        except Exception as e:
            print(f"The item {e} does not exist! Please try a valid number!")
            search_item(product_field)



def search_by_name():
    pass


def search_by_id():
    pass