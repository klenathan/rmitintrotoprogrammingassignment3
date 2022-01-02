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
