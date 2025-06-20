# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class Student:

    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def average(self):
        return (self.sub1+self.sub2+self.sub3)/3
    

s1 = Student("Bilal",30,30,30)

print(s1.average())