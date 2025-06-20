# Make the student management system using pyhton.
# insert, update, delete the student & make the student class to inherit the person class.
# Person class is contain the name, birth date, address & phone number.
# Studen class is contain the Roll no, marks. method print the marksheet, get marks.
class Person:

    def __init__(self, name, birth, address, phone):
        self.name = name
        self.birth = birth
        self.address = address
        self.phone = phone
    
    def setName(self,name):
        self.name = name

    def setBirth(self,birth):
        self.birth = birth

    def setAddress(self,address):
        self.address = address
    
    def setPhone(self,phone):
        self.phone = phone

    def getName(self):
        return self.name
    
    def getBirth(self):
        return self.birth
    
    def getAddress(self):
        return self.address
    
    def getPhone(self):
        return self.phone
    
class Student(Person):

    def __init__(self, roll, name, birth, address, phone, marks):
        super().__init__(name,birth,address,phone)
        self.rollNo = roll
        self.marks = marks

    def setMarks(self,marks):
        self.marks = marks

    def setMarks(self, index, mark):
        self.marks[index] = mark

    def getRollNo(self):
        return self.rollNo
    
    def getMarks(self):
        return self.marks
    
    def marksheet(self):
        print("="*20)
        print("ABCD School Marksheet")
        print("="*20)
        print(f"Roll No: {self.rollNo}")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.birth}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone}")
        print("-"*20)
        sum = 0
        for i in self.marks:
            print({i})
            sum += i
        print(f"Total mark: {sum}")

    @staticmethod
    def menu():
        print("+"*20)
        print("Student System")
        print("+"*20)
        print("Press 1 for insert student")
        print("Press 2 for update student")
        print("Press 3 for delete student")
        print("Press 4 for all students display records")
        print("Press 5 for Marksheet specific student")
        print("Press 6 for exit")

        return int(input("Enter your choice: "))

if __name__ == '__main__':
    students = []
    while True:
        ch = Student.menu()

        if ch == 1:
            print("Insert Student Details")
            roll = input("Enter your roll no: ")
            name = input("Enter your name: ")
            birth = input("Enter your date of birth(DD/MM/YYYY):")
            address = input("Enter your address: ")
            phone = input("Enter your phone number: ")
            
            marks = []
            for i in range(3):
                marks.append(int(input(f"Enter sub{i+1} mark: ")))

            std1 = Student(roll,name,birth,address,phone,marks)
            students.append(std1)
            print("Successfully Inserted!!")
        elif ch == 2:
            roll = input("Enter roll to update: ")

            for student in students:
                if student.getRollNo() == roll:
                    print("Choice to update detail")
                    print("Press 1 for update name")
                    print("Press 2 for update address")
                    print("Press 3 for update phone number")
                    print("Press 4 for update marks")
                    print("Press 5 for exit to home")
                    ch = int(input("Enter your choice: "))

                    if ch == 1:
                        name = input("Enter new name: ")
                        student.setName(name)
                        print(f"new is {student.getName()} updated!!")
                    elif ch == 2:
                        address = input("Enter new address: ")
                        student.setAddress(address)
                        print(f"new is {student.getAddress()} updated!!")
                    elif ch == 3:
                        phone = input("Enter new phone number: ")
                        student.setPhone(phone)
                        print(f"new is {student.getPhone()} updated!!")
                    elif ch == 4:
                        print("Press 1 for update sub1 mark")
                        print("Press 2 for update sub2 mark")
                        print("Press 3 for update sub3 mark")
                        i = int(input("Enter your choice: "))

                        student.setMarks(i-1,int(input(f"Enter the sub{i} new mark: ")))
                        print("Successfully updated!!")
                    elif ch == 5:
                        break
                    else:
                        print("Oops!! wrong choice.")
        elif ch == 3:
            roll = input("Enter roll to delete: ")

            for student in students:
                if student.getRollNo() == roll:
                    students.remove(student)
                    break
            print(f"Successfully roll no: {student.getRollNo()} deleted!!")
        elif ch == 4:
            print("Display All Student Records")
            for st in students:
                print(";"*10)
                print(f"Roll No: {st.getRollNo()}\nName: {st.getName()}\nDate of Birth: {st.getBirth()}\nAddress: {st.getAddress()}\nPhone Number: {st.getPhone()}")
        elif ch == 5:
            roll = input("Enter roll to print the marksheet: ")

            for student in students:
                if student.getRollNo() == roll:
                    student.marksheet()
                    break
        elif ch == 6:
            break
        else:
            print("Wrong choice!!")
            if input("Do you want to countinue 'Y' either 'N': ") != 'Y':
                break