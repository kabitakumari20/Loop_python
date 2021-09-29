num=int(input("enter the num="))
i=2
while i<num:
    b=2
    while b<i:
        if i%2==0:
            print("it is not prime num",i)
            break
        b=b+1
    else:
        print("it is prime num",i)
    i=i+1