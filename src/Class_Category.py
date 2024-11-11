from src.Class_Product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.category_count += 1
        self.product_count = len(products)

    @property
    def add_product(self):
        self.__products.append(f'{Product.name}, {Product.price} руб. Остаток: {Product.quantity} шт.')
        return self.__products


