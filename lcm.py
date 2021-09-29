num=int(input("enter the num="))
num1=int(input("enter the num="))
i=1
while i>0:
    if i%num==0 and i%num1==0:
        lcm=i
        break
    i=i+1
print(lcm)

