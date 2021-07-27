from Person import Person


class Employee(Person):
    def __init__(self, id: int, name: str, age: int, address: str, wage: float):
        super().__init__(id, name, age, address)
        self.__wage = wage


    @property
    def wage(self):
        return self.__wage
