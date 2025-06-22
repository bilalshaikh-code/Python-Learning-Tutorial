import os
import datetime
import math

# Task manager:- Add, Disaplay, Delete those to do in task manager. 
# Add task: input from user - Task name, Description, due date-time (valid format). Defualt save - current date-time non as the created datetime.
class task:

    def __init__(self,name,des,due: datetime.datetime):
        self.name = name
        self.description = des
        self.due_date = due
        self.create_date = datetime.datetime.today()

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
        print("Press 5 for Exit")

        return int(input("Enter your choice: "))

if __name__ == "__main__":
    tasks = []
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
                tasks.append(task1)
                print("Successfully Added Task.")
            case 2:
                print("-"*10+"\nDisplay All Task\n"+"-"*10)
                for tsk in tasks:
                    print(f"Task Name: {tsk.getName()}\nDescription: {tsk.getDescription()}\nDue: {tsk.getDue()}\nCreated Date: {tsk.getCreated()}\nDays remaining: {tsk.getDue() - datetime.datetime.now()}")
                    print("="*10)
            case 3:
                print("-"*10+"\nDelete task\n"+"-"*10)
                name = input("Enter the task name to want to delete: ")
                if input("Verify to enter the delete word: ") != "delete":
                    print(f"{name} is not delete!")
                else:
                    for tsk in tasks:
                        if tsk.getName() == name:
                            tasks.remove(tsk)
                    print("Successfully Deleted!")
            case 4:
                print("-"*10+"\nDeadline Task\n"+"-"*10)
                for tsk in tasks:
                    if (tsk.getDue() - datetime.datetime.now()).days >= 0 and (tsk.getDue() - datetime.datetime.now()).days <= 1:
                        print(f"Task Name: {tsk.getName()}\nDescription: {tsk.getDescription()}\nRemaining Days/Time: {tsk.getDue() - datetime.datetime.now()}")
            case 5:
                break