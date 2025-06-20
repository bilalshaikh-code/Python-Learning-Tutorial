# Topic
# Python basics (variables, loops, condition)

while True:
    print("*"*20+"\nSimple Calculator"+"\n"+"*"*20)

    print("Press 1 for Add")
    print("Press 2 for Sub")
    print("Press 3 for Mul")
    print("Press 4 for Div")
    print("Press 5 for Exit")
    ch = int(input("Enter your choose: "))

    if ch == 5:
        break

    num1 = int(input("Enter the number 1: "))
    num2 = int(input("Enter the number 2: "))
    ans = 0

    if(ch == 1):
        ans = num1+num2
        seing = '+'
    elif(ch == 2):
        ans = num1-num2
        seing = '-'
    elif(ch == 3):
        ans = num1*num2
        seing = 'X'
    elif(ch == 4):
        ans = num1/num2
        seing = '/'
    else:
        print("Wrong choose.")
    
    print(f"{num1} {seing} {num2} = {ans}")