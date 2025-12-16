#Abstraction means hiding internal details and showing only what is needed.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike starts")

b = Bike()
b.start()
