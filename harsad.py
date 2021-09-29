num=int(input("enter the num="))
n=num
sum=0
rem=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10 
    print(sum)
    res=n%sum
if res==0:
    print("it is harsad num",n)
else:
    print("it is not harsad num",n)


