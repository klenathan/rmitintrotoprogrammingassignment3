FAQ_Dict = {
    "Where can I check the delivery?": "\nWe don't support any services to track the location, but the customer is able to receive the current status through message.",
    "\nWhat do I need if I want to refund the product?": "\nIn order to get refund, you need order id and the name of customer.",
    "\nCan I request additional books that are not on the list?": "\nIf there are many requests, we will add them after reviewing them.",
    "\nHow can I get the discount?": "\nThe discount rate is be based on the previous purchase history, and 10% is the max discount.",
    "\nHow can I rate a book?": "\nPeople that have purchased a book can only rate a book.",
    "\nCan I purchase a digital book?": "\nWe don't support any digital version of a book. This feature will be added later on.",
    "\nHow can I pay money?": "\nThere are credit card, bank transfer in payment method. More options will be added later.",
    "\nWhen can I get my book?": "\nNormally, it will take 2 ~ 3 days, but it can be up to 7 days depends on the location.",
    "\nWhat's the standard for best selling books?": "\nIt depends on the rating and the amount of sold quantities. It will be updated every month",
    "\nHow to find a book that I want to search in detail?": "\nYou should know the name, or item id",
    "\nWhat if it is out of stock?": "\nWe will check the quantity every time, but the customer can request it if the stock is not supplemented."
}
question_and_answer_list = FAQ_Dict.items()

for key, value in question_and_answer_list:
    print(key, value)
