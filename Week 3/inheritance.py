# Inheritance
# *Inheritance: The process by which derived class acquires the characteristics  of a base class.*
# *Children class* as *Derived class*
# *Parent class* as *Base class*
# Types of inheritance
# Single inheritance: Children class inheritance from a parent class.
# Multiple: Children class inheritance from multiple parents classes.
# Multilevel: Children class inheritance from another children class.

# Single inheritance:
class Car:
    color = "Black"

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stoped..")

class Toyota(Car):
    def __init__(self,name):
        self.name = name

car1 = Toyota("fortuner")
car2 = Toyota("prius")

print(car1.color)