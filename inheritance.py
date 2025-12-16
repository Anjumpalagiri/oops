#inheritance
#Inheritance means one class uses properties and methods of another class.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()

