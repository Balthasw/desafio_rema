class Sale:
    def __init__(self, id_sale: int, id_product: int, id_customer: int,
                 quantity: int, final_price: float):
        self.__id_sale = id_sale
        self.__id_product = id_product
        self.__id_customer = id_customer
        self.__quantity = quantity
        self.__final_price = final_price

    @property
    def id_sale(self):
        return self.__id_sale

    @property
    def id_product(self):
        return self.__id_product

    @property
    def id_customer(self):
        return self.__id_customer

    @property
    def quantity(self):
        return self.__quantity

    @property
    def final_price(self):
        return self.__final_price
