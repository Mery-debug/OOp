from ctypes import Union


class Product:
    name: str
    description: str
    price: int
    quantity: int
    product: dict
    list_of_product: list

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
    def new_price(self) -> int:
        return self.price

    @new_price.setter
    def new_price(self, value: int):
        if value <= 0:
            print('Цена не должна быть нулевая или отрицательная')
