i=1
my_num=5
while i<9:
    num=int(input("enter the num="))
    if num>my_num:
        print(num,"grater than my _num")
    elif num<my_num:
        print(num,"less than my_num")
    elif num==my_num:
        print("well guse")
        break
    else:
        print("wrong grss")
    i=i+1