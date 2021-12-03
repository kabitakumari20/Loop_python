import abc


# a=4+3%5
# print(a)

num=int(input("enter the num:-"))
my_number=5
i=1
while i<=num:
    num1=int(input("Enter the num:-"))
    if num1>my_number:
        print("num1 is grater then my num")
    elif num1<my_number:
        print("my num is grater then num1")
    elif num1==my_number:
        print("congralation u are win")
    else:
        print("u loss ur game")
    i=i+1

