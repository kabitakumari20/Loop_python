num=int(input("enter the num"))
i=0
while num>0:
    a=num//10
    if a%10==7:
        print("yes")
    else:
        print("no:")
    i=i+1
    num=num-num
    
