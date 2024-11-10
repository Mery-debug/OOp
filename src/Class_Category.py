class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.category_count += 1
        self.product_count = len(products)


# def category_products() -> Category:
#     return Category('fruits', 'som sweets', ['apple', 'banana', 'orange'])
#
#
# y = category_products().category_count
# x = category_products().product_count
#
# print(y, x)
