from Person import Person


class Customer(Person):
    def __init__(self, id: int, name: str, age: int, address: str):
        super().__init__(id, name, age, address)
