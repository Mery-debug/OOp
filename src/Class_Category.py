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
    def products_list(self):
        for product in self.__products:
            self.__products.append(f'{product}, {product} руб. Остаток: {product} шт.')
        return self.__products

    def add_product(self, product: Product):
        self.__products.append(product)
        self.category_count += 1


