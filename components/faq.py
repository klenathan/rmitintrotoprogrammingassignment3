import json

def faq():
    with open('data/faq.json', 'r', encoding='utf-8') as faq_file:
        faq = json.load(faq_file)

    question_and_answer_list = faq.items()

    for key, value in question_and_answer_list:
        print(key, value)

faq()