


# Search

def search_by_name(data, book_name):
    for id in data["product"]:
        title = data["product"][id]["title"]
        if title == book_name:
            return id
        else:
            print("Invalid book name! Please try again")
            ### ADD option to keep searching
            return None


def search_by_id(data, field, search_id):
    return data[field][search_id]
