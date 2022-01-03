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
        i = 1
        # Loop through the faq dictionary
        for key, value in faq_data.items():
            print(f'{Style.BOLD}{i}. {key}{Style.END}\n- {value}\n')
            i += 1
        
        input('Press any key to go back ')
        cls()
        break
