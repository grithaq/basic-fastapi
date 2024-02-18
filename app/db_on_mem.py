class Product():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id} {self.name} {self.price}"
    

class ListProduct():
    products = []

    def get_products(self):
        return self.products
    
    def add_product(self, product):
        self.products.append(product)
        return f"{product.name} was added"
    
    def find_product_index(self, product_id: int):
        for index, product in enumerate(self.products):
            if product.id == product_id:
                return index
        return -1  # Product not found
    
    def update_product(self, product_id: int, new_product: Product):
        for index, product in enumerate(self.products):
            if int(product_id) == self.products[index]['id']:
                self.products[index] = new_product
                return f"{new_product.name} was added"
        return "product is not found"

    
    def delete_product(self, product_id: int):
        index = self.find_product_index(product_id)
        if index != -1:
            del self.products[index]
            return f"Product with ID {product_id} was deleted"
        else:
            return f"Product with ID {product_id} not found"
        
db_product = ListProduct()