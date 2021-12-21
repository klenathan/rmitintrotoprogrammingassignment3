

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


def search_by_id(data, field, search_id):
    return data[field][search_id]
