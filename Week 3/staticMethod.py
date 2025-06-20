# Static Method
# Method that don't use the *self* parameter (work at class level).
# define static method: *@staticmethod* before define the *def*.
class Student:

    @staticmethod  #decorator
    def hello():
        print("hello")

s1 = Student()
s1.hello()