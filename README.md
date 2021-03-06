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
- Discount (Integrate in ordering process)
- Return shipment
- Product review
- Best seller product ranking
- Purchase history (Integrate with list all information from a specific customer)
### Json file structure
``` yaml
data.json
{
    "product": {
        product_id: {
            "title": product_title,
            "quantity": product_quantity,
            "sold": sold_amount,
            "description": product_desc,
            "price": price,
            "author": author,
            "rating": {
                "total_point": 0,
                "num_of_review": 0,
                "average": 0
            }
        }
    },
    "customer": {
        customer_id: {
            "id": customer_id,
            "name": customer_name,
            "email": customer_email,
            "phone_num": customer_phone_num,
            "address": customer_add,
            "order": {
                order_id: {
                    "product_id": product_id,
                    "quantity": bought_quantity,
                    "total_cost": total_cost,
                }
            }
        }
    },
    "order": {
        order_id: {
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": bought_quantity,
            "total_cost": total_cost,
            "customer_address": customer_address,
            "reviewed": reviewed
        }
    },
    "return": {
        order_id: {
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": bought_quantity,
            "total_cost": total_cost,
            "customer_address": customer_address,
            "reason of return": reason
        }
    }
}
```
