import os
import datetime
import math

# Task manager:- Add, Disaplay, Delete those to do in task manager. 
# Add task: input from user - Task name, Description, due date-time (valid format). Defualt save - current date-time non as the created datetime.
class task:

    def __init__(self,name,des,due):
        self.name = name
        self.description = des
        self.due_date = due
        self.create_date = datetime.datetime.today()

    def addTask(self):
        ...

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getDue(self):
        return self.due_date
    
    def getCreated(self):
        return self.create_date

    @staticmethod
    def menu():
        print("-"*12)
        print("Task Manager")
        print("-"*12)
        print("Press 1 for Add task")
        print("Press 2 for Display all task")
        print("Press 3 for Delete task")
        print("Press 4 for Check how much time is left until deadline")
        print("Press 5 for Use basic stats(e.g. task urgency, days left)")
        print("Press 6 for Exit")

        return int(input("Enter your choice: "))

if __name__ == "__main__":
    taskes = []
    while True:
        ch = task.menu()

        match ch:
            case 1:
                print("-"*10+"\nAdd Task\n"+"-"*10)
                name = input("Enter the task name: ")
                des = input("Enter the description: ")
                due = input("Enter the due date time(dd/mm/yyyy HH:MM:SS): ")
                try:
                    format = datetime.datetime.strptime(due,"""%d/%m/%Y %H:%M:%S""")
                except Exception:
                    print(f"{due} format is invalid or date-time is invalid!!")
                task1 = task(name,des,format)
                taskes.append(task1)
                print("Successfully Added Task.")
            case 2:
                print("-"*10+"\nDisplay All Task\n"+"-"*10)
                for tsk in taskes:
                    print(f"Task Name: {tsk.getName()}\nDescription: {tsk.getDescription()}\nDue: {tsk.getDue()}\nCreated Date: {tsk.getCreated()}")
                    print("="*10)
            case 3:
                print("-"*10+"\nDelete task\n"+"-"*10)
                name = input("Enter the task name to want to delete: ")
                if input("Verify to enter the delete word: ") != "delete":
                    print(f"{name} is not delete!")
                    
                for tsk in taskes:
                    if tsk.getName() == name:
                        taskes.remove(tsk)
                print("Successfully Deleted!")
            case 4:
                ...
            case 5:
                ...
            case 6:
                break