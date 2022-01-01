import json
from components.cls import cls
from prettytable import PrettyTable


def handle_review(json_data):
    """
    The function takes review from customer and write to database
    :param: 
        json_data: dictionary containing all data from database (dict)
    :return: None
    """
    while True:
        try:
            order_id = input("What was your order id? ")
            # Check if order exist
            if json_data["order"][order_id]:
                # Check if order is reviewed
                # If order is reviewed, customer go back to main menu
                if json_data["order"][order_id]["reviewed"] != "False":
                    print("The order has been rated")
                    user_opt = input(
                        "Press 0 to go back or any key to try again\n")
                    if user_opt == "0":
                        cls()
                        break
                # Forward to review process
                else:
                    product_id = json_data["order"][order_id]["product_id"]
                    total_point = json_data["product"][product_id]["rating"]["total_point"]
                    num_of_review = json_data["product"][product_id]["rating"]["num_of_review"]
                    # Print order details to console
                    print("\nOrder details")
                    print(f'Product id: {product_id}')
                    print(
                        f'Book title: {json_data["product"][product_id]["title"]}')
                    print(
                        f'Bought quantity: {json_data["order"][order_id]["quantity"]}')
                    # Get user's review
                    user_review = int(
                        input("\nHow do you rate the product from 1 to 5? "))
                    average_point = 0

                    # Check if review input is valid (in range from 1 to 5)
                    if user_review > 5 or user_review < 1:
                        print('Invalid rating, please try again ')
                        continue
                    else:
                        total_point += user_review
                        num_of_review += 1
                        average_point = total_point/num_of_review
                        # Update rating dictionary of the product
                        rating_dict = {
                            "total_point": total_point,
                            "num_of_review": num_of_review,
                            "average": average_point
                        }
                        json_data['product'][product_id]['rating'] = rating_dict
                        json_data["order"][order_id]["reviewed"] = "True"
                        # Write data to file
                        json_file = open('data/data.json', 'w')
                        json.dump(json_data, json_file, indent=4)
                        # Clear console & thank you
                        cls()
                        print("Thank you for your review, press any key to go back")
                        break
        except Exception as e:
            print(f'Order ID {e} does not exist')
            try_again_opt = input(
                "Type 0 to go back to main menu, any other key to try again\n")
            if try_again_opt == "0":
                cls()
                break


def discount(json_data, customer_id_input):
    """
    The function calculates discount based on previous orders from a specific customer
    :param:
        json_data: dictionary containing all data from database (dict)
        customer_id_input: customer_id of the purchasing customer (str)
    :return:
        discount_rate: calculated discount rate (int)
    """
    discount_rate = 0
    total_items = 0

    # loop through order dictionary
    for order_id in json_data['order']:
        customer_id = json_data['order'][order_id]['customer_id']

        if customer_id_input == customer_id:
            # calculate the total books a customer had bought
            total_items += int(json_data['order'][order_id]['quantity'])

            # the discount rate is applied for the next order
            # if the total items meet the requirement
            if total_items >= 50:
                discount_rate = 10
            elif total_items >= 40:
                discount_rate = 5
            elif total_items >= 30:
                discount_rate = 3

    return discount_rate


def return_shipment(json_data):
    """
    The function logs return request from customer to the database
    :param: 
        json_data: dictionary containing all data from database (dict)
    :return: None
    """
    # Clear console
    cls()
    while True:
        try:
            order_id = input("\nPlease input your order id: ")
            if order_id in json_data['order']:
                return_reason = input(
                    "What is your reason of return? ")
                json_data['return'][order_id] = json_data['order'][order_id].copy()
                json_data['return'][order_id].pop("reviewed")
                json_data['return'][order_id]["reason_of_return"] = return_reason
                json_data['order'].pop(order_id)
                # Write to data file
                json_file = open('data/data.json', 'w')
                json.dump(json_data, json_file, indent=4)
                cls()
                print(
                    '\nSorry for your inconvenience.\nWe will process your request as soon as possible')
                break
            else:
                print("Order does not exist")
            break
        except Exception as e:
            print(f'Order {e} does not exist')
            print("\n0. Exit")
            print("1. Try again")
            if input("Type 0 to go back to main menu, any other key to try again ") == "0":
                cls()
                break


def best_books(json_data):
    """
    The function displays best-selling books rank
    :param: 
        json_data: dictionary containing all data from database (dict)
    :return: None
    """
    while True:
        try:
            sorted_sold = sorted(json_data['product'],
                                 key=lambda item: json_data['product'][item]["sold"],
                                 reverse=True)

            table = PrettyTable(
                ['ID', 'Book Title', 'Author', 'Quantity', 'Price', "Rating", "Sold"])
            table.align = 'l'

            for id in sorted_sold:
                table.add_row([
                    id,
                    json_data['product'][id]['title'],
                    json_data['product'][id]['author'],
                    json_data['product'][id]['quantity'],
                    json_data['product'][id]['price'],
                    f'{json_data["product"][id]["rating"]["average"]:.2f}',
                    json_data['product'][id]['sold'],
                ])
            print(table)
            input("Press any key to go back to main menu ")
            cls()
            break
        except Exception as e:
            print(e)
            break
