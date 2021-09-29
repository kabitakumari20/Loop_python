num=int(input("enter the number"))
a=num
j=0
while num>0:
    var=num%10
    j=j*10+var
    num=num//10
if a==j:
    print("it is palindrome number")
else:
    print("it is not palindrom number")





i=int(input("enter the any number"))
rev=0
x=i
while i>0:
    rev=rev*10+i%10
    i=i//10
if x==rev:
    print("palindrome number")   
else:a