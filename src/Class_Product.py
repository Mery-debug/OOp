from ctypes import Union


class Product:
    name: str
    description: str
    price: int
    quantity: int
    product: dict
    product_lst = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, n_product: dict):
        new = cls(**n_product)
        if new.name == Product.name:
            Product.quantity = Product.quantity + n_product.get('quantity')
            if Product.price > n_product.get('price'):
                Product.__price = Product.price
            elif Product.price < n_product.get('price'):
                Product.__price = n_product.get('price')
            else:
                Product.__price = Product.price
        return new





    @property
    def new_price(self) -> int:
        return self.price

    @new_price.setter
    def new_price(self, value: int):
        if value <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        elif self.__price > value:
            i = input(f'Цена понижается с {self.__price} по {value}. Подтверждаете? (y/n)')
            if i.lower() == 'y':
                self.__price = value
            elif i.lower() == 'n':
                self.__price = self.__price
            else:
                print('Ошибка ввода, нет такого варианта.')




