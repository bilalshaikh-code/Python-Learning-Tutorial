# Constructor
# All classes have a function called __init__(), whaich is always executed when the class is being initiated.
# Must be *self* pass as the parameter for any class function. this parameter is refernce to the current instance of the class.
class Student:
    # Class attribute is one time to store in memory for every object. means the *college_name* attribute same for all object. this class attribute is different way to access first the access class_name.attribute_name and second object_name.attribute_name.
    college_name = "ABC College" # Class attribute

    def __init__(self,fullName):
        # Object attribute is based on object to store in memory. means the *self.name* is object attribute is very object to new or every object to store different values on object based. this object attribute on access by object_name.attribute_name. object attribute > class attribute
        self.name = fullName # Object attribute
        print("adding new student in database...")

s1 = Student("karan")
print(s1.name)

s2 = Student("arjun")
print(s2.name) # Object attribute

print(Student.college_name) # Class attribute