from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        pass


class MixinLog:

    def __init__(self):
        self.__repr__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinLog, ABC):
    """
    Класс продукты, в котором есть имя продукта, описание, цена и количество на складе,
    есть строковое отображение
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if quantity == 0:
            raise ZeroDivisionError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()
        print(repr(self))

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
        if not isinstance(other, Product):
            raise TypeError
        else:
            add = self.__price * self.quantity + other.price * other.quantity
            return add


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency: str = efficiency
        self.model: str = model
        self.memory: str = memory
        self.color: str = color

    def __add__(self, other):
        super().__add__(other)
        if not isinstance(other, Smartphone):
            raise TypeError
        else:
            add = self.price * self.quantity + other.price * other.quantity
            return add


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country: str = country
        self.germination_period: str = germination_period
        self.color: str = color

    def __add__(self, other):
        super().__add__(other)
        if not isinstance(other, LawnGrass):
            raise TypeError
        else:
            add = self.price * self.quantity + other.price * other.quantity
            return add


# class NullExceptionQuantity(BaseException, Product):


    # def __init__(self):
    #     super().__init__()
    # def null_quantity(self):
    #
    #     if Product.quantity == 0:
