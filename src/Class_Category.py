class Category:
    name: str
    description: str
    products: list

    category_item = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.category_item += 1

    def category_count(self):
        return self.category_item

    def product_count(self):
        return len(self.products)
