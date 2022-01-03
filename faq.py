import json
from components.styling import Style
from components.cls import cls

question_list = ["Where can I check the delivery?", "What do I need if I want to refund the product?",
                 "Can I request additional books that are not on the list?", "How can I get the discount?",
                 "How can I rate a book?", "Can I purchase a digital book?", "When can I get my book?",
                 "What's the standard for best selling books?", "How to find a book that I want to search in detail?",
                 "What if it is out of stock?", "Other"]


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
        for key in faq_data.keys():
            print(f'{Style.BOLD}{i}. {key}')
            i += 1

        user_option = input(
            'Write down the number that you want to know about, or press 0 to quit.')
        while True:
            cls()
            print(faq_data.get(question_list[int(user_option) - 1]))
            break

        if user_option == "11":
            cls()
            print('Please write down your questions. '
                  'The submitted question will be stored in the data and will be '
                  'considered '
                  'later :')
            f = open('Question from customers.txt', 'a', encoding='utf-8')
            f.write(input())
            f.write('\n')
            f.close
            print()
            cls()

        if user_option == "0":
            cls()
            break
