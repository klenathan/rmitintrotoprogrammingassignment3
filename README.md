# RMIT Intro to Programming Assignment 3
----
### Project is done by group 9<br>
Tran Nam Thai<br>
Pham Anh Thu <br>
Nguyen Duong Truong Thinh<br>
Jang Soohyuk<br>

### Main features
- List all items
- Search item by name
- Search item by item id 
- List all information of a specific customer
- Placing orders
### Additional features
- Payment management
- Discount
- Return shipment
- Product review
### Json file structure
``` yaml
data.json
{
    "product": {
        product_id: {
            "title": product_title,
            "quantity": product_quantity,
            "description": product_desc,
            "price": price,
            "author": author",
            "rating": {
                "total_point": 0,
                "num_of_review": 0,
                "average": "No Review"
            }
        }
    },
    "customer": {
        customer_id: {
            "id": customer_id,
            "name": customer_name,
            "email": customer_email,
            "phone_num": customer_phone_num,
            "address": customer_add
        }
    },
    "order": {
        order_id: {
            "id": order_id,
            "customer_id": customer_id,
            "product_id": product_id,
            "customer_address": customer_address
        }
    },
    "return": {
        "order_id": {
            "customer name": "customer_name",
            "reason of return": "reason"
        }
    }
}
```