
class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, n_product: dict):
        new = cls(**n_product)
        return new

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value > 0:
            self.__price = value
        elif value <= 0:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт'

    def __add__(self, other):
        add = self.__price * self.quantity + other.price * other.quantity
        return add

# product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
# product4.price = -1
# print(product4.price)
