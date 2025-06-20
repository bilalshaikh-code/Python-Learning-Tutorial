# Methods
# Function is as the method to in class.
# Must be *self* pass as the parameter for any class function. this parameter is refernce to the current instance of the class.
class Student:

    def __init__(self,name):
        self.name = name

    def welcome(self):
        print("Welcome, "+self.name)

s1 = Student("karan")
s1.welcome()