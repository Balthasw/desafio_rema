from abc import ABC, abstractmethod


# Abstract class for customer and employee
class Person(ABC):
    @abstractmethod
    def __init__(self, id: int, name: str, age: int, address: str):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__address = address

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def address(self):
        return self.__address
