from src.Class_Product import Product, Smartphone


class Category:
    """
    Класс категория, в котором есть имя категории, список продуктов,
    описание, счетчики категории и продуктов. Так же частично работает с классом продукты из product.py
    """
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.__products: list = products
        self.category_count += 1
        self.product_count = len(products)

    @property
    def products(self):
        product_str = []
        for product in self.__products:
            product_str.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return product_str

    def add_product(self, product: Product):
        if issubclass(type(product), Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise TypeError

    def __str__(self):
        product_sum = 0
        for product in self.__products:
            if self.name:
                product_sum += product.quantity
        return f'{self.name}, количество продуктов: {product_sum}'

    def avg_sum_cat(self):
        try:
            avg_sum = sum(product for product in self.__products)
            return avg_sum / len(self.__products)
        except ZeroDivisionError:
            return 0
