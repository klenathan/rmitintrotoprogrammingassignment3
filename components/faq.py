import json
from components.styling import Style
from components.cls import cls

def faq():
    '''
    The function print frequently asked question from faq.json file
    '''
    while True:
        with open('data/faq.json', 'r', encoding='utf-8') as faq_file:
            faq = json.load(faq_file)
        i = 1
        question_and_answer_list = faq.items()

        for key, value in question_and_answer_list:
            print(f'{Style.BOLD}{i}. {key}{Style.END}\n- {value}\n')
            i += 1
        input('Press any key to go back')
        cls()
        break