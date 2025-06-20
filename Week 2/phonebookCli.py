# Topic
# Functions, lists, tuples, dictionaries

# PhoneBook : Create, Edit, Remove, Display & search.

def phoneBook():
    phbList = []

    while True:
        ch = menu()

        if ch == 1:
            phbList = create(phbList)
        elif ch == 2:
            phbList = edit(phbList)
        elif ch == 3:
            phbList = remove(phbList)
        elif ch == 4:
            display(phbList)
        elif ch == 5:
            search(phbList)
        elif ch == 6:
            break
        else:
            print("Wrong choice!!")

def menu():
    print("-"*20+"\nPhone Book"+"\n"+"-"*20)
    print("Press 1 for Create the contact")
    print("Press 2 for Edit the contact")
    print("Press 3 for Remove the contact")
    print("Press 4 for Display all the contacts")
    print("Press 5 for Search the contact")
    print("Press 6 for exit")

    return int(input("Enter your choice: "))

def create(oldList: list):
    # name, phone number - required
    # email, date of birth, category[friend, family, work, other] - Option
    while True:
        print("Create a contact")
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        if name != None and phone != None:
            break    
        print("Enter the Name or Phone number is required!")
    
    birth_date = input("Enter the birth date (Option): ")
    email = input("Enter the email (Option): ")
    
    while True:
        print("Select anyone category\nPress 1 for Friend")
        print("Press 2 for Family")
        print("Press 3 for Work")
        print("Press 4 for Other")
        category = input("Enter the Category (Option): ")

        if category != '':
            if category != '1' and category != '2' and category != '3' and category != '4':
                print("Wrong choice!!")
            else:
                if category == '1':
                    category = "Friend"
                elif category == '2':
                    category = "Family"
                elif category == '3':
                    category = "Work"
                elif category == '4':
                    category = "Other"
                break
        else:
            break

    oldList.append({
        'name': name,
        "phone" : phone,
        'birth_date' : birth_date or None,
        'email' : email or None,
        'category' :  category or None
    })
    print("Successfully created!!")
    return oldList

def edit(oldList: list):
    print("Edit a contact")
    name = input("Enter the name to want to update: ")
    newList = []
    for contact in oldList:
        if name == contact['name']:
            while True:
                print("Press 1 for update the name")
                print("Press 2 for update the phone")
                print("Press 3 for update the birth date")
                print("Press 4 for update the email")
                print("Press 5 for update the category")
                print("Press 6 for exit to home")
                ch = int(input("Enter the your choice: "))

                if ch != 1 and ch != 2 and ch != 3 and ch != 4 and ch != 5 and ch != 6:
                    print("Wrong choice!!")
                else:
                    break
            if ch == 1:
                contact['name'] = input("Enter new name: ")
            elif ch == 2:
                 contact['phone'] = input("Enter new phone number: ")
            elif ch == 3:
                contact['birth_date'] = input("Enter new birth date: ")
            elif ch == 4:
                contact['email'] = input("Enter new email: ")
            elif ch == 5:
                while True:
                    print("Select anyone category\nPress 1 for Friend")
                    print("Press 2 for Family")
                    print("Press 3 for Work")
                    print("Press 4 for Other")
                    category = input("Enter the Category (Option): ")

                    if category != '':
                        if category != '1' and category != '2' and category != '3' and category != '4':
                            print("Wrong choice!!")
                        else:
                            if category == '1':
                                category = "Friend"
                            elif category == '2':
                                category = "Family"
                            elif category == '3':
                                category = "Work"
                            elif category == '4':
                                category = "Other"
                            break
                    else:
                        break
                contact['category'] = category
            elif ch == 6:
                return oldList
            newList.append(contact)
        else:
            newList.append(contact)
        print("Successfully Updated!!")
    return newList

def remove(oldList: list):
    print("Remove a contact")
    name = input("Enter the name to want to delete: ")
    if input("Enter the delete word: ") != 'delete':
        print("Contact is not delete!")
        return oldList
    newList = []
    for contact in oldList:
        if name != contact['name']:
            newList.append(contact)
    print("Successfully Deleted!!")
    return newList

def display(oldList):
    for contact in oldList:
        print("*"*5)
        print(f"Name: {contact["name"]} \nPhone Number: {contact["phone"]} \nBirth Date: {contact['birth_date']} \nEmail: {contact['email']} \ncategory: {contact['category']}")
    
def search(oldList: list):
    print("Search a contact")
    name = input("Enter the name to want to search: ")
    notFound = True
    for contact in oldList:
        if name == contact['name']:
            print(f"Name: {contact["name"]} \nPhone Number: {contact["phone"]} \nBirth Date: {contact['birth_date']} \nEmail: {contact['email']} \ncategory: {contact['category']}")
            notFound = False
    
    if notFound == True:
        print(f"{name} is not found!!")

if __name__ == '__main__':
    phoneBook()