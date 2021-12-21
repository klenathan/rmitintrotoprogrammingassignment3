

# Search

def search_by_name(data):
    user_input = input("\nBook name?: ")
    for id in data["product"]:
        title = data["product"][id]["title"]
        if title == user_input:
            return id
        else:
            print("Not found")
            ### ADD option to keep searching
            return None


def search_by_id(data):
    user_input = input('\nBook Id?: ')
    if int(user_input) <= 5:
        return data['product'][user_input]
    else:
        return None
