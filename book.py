import json
import tqdm

class book:
    def __init__(self, data, id):
        self.id = id
        self.title = data["product"][id]["title"]
        self.quantity = data["product"][id]["quantity"]
        self.description = data["product"][id]["description"]
        self.price = data["product"][id]["price"]
        self.author = data["product"][id]["author"]

    def list_item(self):
        for i in tqdm(self.data["product"]):
            book_title = self.data["product"][i]["title"]
            print(f'{i}. {book_title}')

    def get_info(self):
        book_id = self.data["product"][self.id]
        print(f'product id: {self.id}')
        for i in book_id:
            print(f'{i}: {book_id[i]}')
        print('\n')