api_keys = {
        "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8",
        "5f0c7127-3be9-4488-b801-c7b6415b45e9": "mUP7PpTHmFAkxcQLWKMY8t"
    }
    
users = {
        "7oDYjo3d9r58EJKYi5x4E8": {
            "name": "Bob"
        },
        "mUP7PpTHmFAkxcQLWKMY8t": {
            "name": "Alice"
        },
    }

products = [
    {"id":1, "name": "Shampo Nature", "price": 26000},
    {"id":2, "name": "Sabun Garnier", "price": 32000},

]

def check_api_key(api_key: str):
    return api_key in api_keys

def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]

def get_products():
    return products

def add_product(product):
    products.append(product)
    return products

def get_product(id: int):
    return products[id]

def update_product(p_id, product):
    for p in products:
        if p["id"] == p_id:
            p["id"] = product["id"]
            p["name"] = product["name"]
            p["price"] = product["price"]
    return products
    
def delete_product(p_id):
    for p in enumerate(products):
        if p[1]['id'] == int(p_id):
            products.pop(p[0])
    return products