def fibonacci():
    n=int(input("enter the num:-"))
    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    print(b)

fibonacci()

num=int(input("Enter the num:-"))
a=0
b=1
i=1
while i<num:
    c=a+b
    a=b
    b=c
    i=i+1
    print(b)