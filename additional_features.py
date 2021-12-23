import json
from cls import cls

def handle_review(json_data):
    order_id = input("What was your order id? ")
    if json_data["order"][order_id]:
        product_id = json_data["order"][order_id]["product_id"]
        total_point = json_data["product"][product_id]["rating"]["total_point"]
        num_of_review = json_data["product"][product_id]["rating"]["num_of_review"]

        print("\nOrder details")
        print(f'Product id: {product_id}')
        print(f'Book title: {json_data["product"][product_id]["title"]}')
        print(f'Bought quantity: {json_data["order"][order_id]["quantity"]}')
        
        user_review = int(input("\nHow do you rate the product from 1 to 5? "))
        if user_review > 5:
            user_review == 5
        elif user_review < 1:
            user_review == 1
        
        total_point += user_review
        num_of_review += 1
        average_point = total_point/num_of_review

        rating_dict = {
            "total_point": total_point,
            "num_of_review": num_of_review,
            "average": average_point
        }
        json_data['product'][product_id]['rating'] = rating_dict
        json_file = open('data.json', 'w')
        json.dump(json_data, json_file, indent=4)
        cls()
    else:
        print("Invalid customer ID")
        input("Press any key to go back")

def discount(json_data, customer_id_input):
    '''
    The function calculate discount based on previous orders from specific customer
    :param: 
        dict: json_data: dictionary contain all information
        str: customer_id_input: customer_id of the purchasing customer
    :return:
        int: discount: calculated discount rate
    '''
    discount = 0
    for order_id in json_data['order']:
        customer_id = json_data['order'][order_id]['customer_id']
        if customer_id_input == customer_id:
            total_items = int(json_data['order'][order_id]['quantity'])

    if total_items >= 10:
        discount = 10
    elif total_items >= 5:
        discount = 5
    elif total_items >= 3:
        discount = 3
    
    return discount

def return_shipment(json_data):
    order_exist = 0
    cls()
    while True:
        order_id = input("Please input your order id: ")
        for i in json_data['order']:
            if i == order_id:
                order_exist += 1
                customer_name = input("What is the buyer's name? ")
                return_reason = input("What is your reason of return? ")
                json_data['return'][order_id] = {
                    "customer name": customer_name,
                    "reason of return": return_reason
                }
                json_file = open('data.json', 'w')
                json.dump(json_data, json_file, indent=4)
                print(
                    '\nSorry for your inconvinient.\nWe will process your request as soon as possible')
                input("Press any key to bo gack: ")

                cls()
                break
        if order_exist == 0:
            print('Order does not exist')
            print("\n 0. Exit")
            print("1. Try again")
            if input("Try again? ") == "1":
                return_shipment(json_data)
                break
        cls()
        break
