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
# Last modified date: 03/01/2022
# Python version: 3.10.0


import json
from components.styling import Style
from components.cls import cls


def faq():
    """
    The function prints frequently asked question from faq.json file
    :param: None
    :return: None
    """
    while True:
        # Open faq data file and decode to JSON
        with open('data/faq.json', 'r', encoding='utf-8') as faq_file:
            faq_data = json.load(faq_file)

        # Loop through the faq dictionary
        i = 1
        for k in faq_data["faq"].keys():
            print(f'{Style.BOLD}{i}. {faq_data["faq"][k]["q"]}{Style.END}')
            i += 1
        # Get user's input
        user_option = input(
            '\nChoose a question you want to know more\nPress 0 to quit\nC for custom question\nYour option: ')
        # Selections
        try:
            if user_option.lower() == "C".lower():
                # Get user's question input
                custom_question = input('\nPlease write down your questions. '
                                        'The submitted question will be stored in our database and will be answered later. \n')
                # Generate new question id
                newid = int(list(faq_data["custom"].keys())[-1]) + 1
                # Write data to dict
                faq_data["custom"][newid] = custom_question
                # Write data to file
                with open('data/faq.json', 'w', encoding='utf-8') as faq_file:
                    json.dump(faq_data, faq_file, indent=4)
                input("Press any key to continue ")
                cls()
            elif user_option == "0":
                cls()
                break
            elif user_option in faq_data["faq"]:
                # Print data based on user's option
                print("")
                print(f'- {Style.BOLD}{faq_data["faq"][user_option]["q"]}{Style.END}')
                print(f'->{Style.BOLD}{faq_data["faq"][user_option]["a"]}{Style.END}')
                input("\nPress any key to continue ")
                cls()
            else: 
                print(f'{Style.RED}{"Invalid input! Please try again!"}{Style.END}')
                print()
        # Print Errors
        except Exception as e:
            print(e)
