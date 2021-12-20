import json

with open('data.json') as json_file:
        json_data = json.load(json_file)
        product_field = json_data['product']

class book:
    def __init__(self, id):
        self.id = id
        self.title = product_field[id]["title"]
        self.quantity = product_field[id]["quantity"]
        self.description = product_field[id]["description"]
        self.price = product_field[id]["price"]
        self.author = product_field[id]["author"]

    def list_item(self):
        for i in product_field:
            book_title = product_field[i]["title"]
            print(f'{i}. {book_title}')

    def get_info(self):
        print('\n')
        book_title = product_field[self.id]
        print(f'product id: {self.id}')
        for i in book_title:
            print(f'{i}: {book_title[i]}')
        print('\n')

class customer:
    def __init__(self, name, email, phone_num, address):
        pass

# Search function
def search_by_name(field, search_name):
    for id in json_data[field]:
        title = json_data[field][id]["title"]
        if title == search_name:
            return id

def search_by_id(field, search_id):
    return json_data[field][search_id]


# book("2").get_info()

# command = input("Type in command: ")