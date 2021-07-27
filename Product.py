class Product:
    def __init__(self, id: int, name: str, price: float, stock_quantity: int):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock_quantity(self):
        return self.__stock_quantity
