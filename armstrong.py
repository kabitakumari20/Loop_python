# num=int(input("enter the num"))
# sum=0
# b=num
# while num>0:
#     rem=num%10
#     var=rem**3
#     sum=sum+var
#     num=num//10
# print(sum)
# if sum==b:
#     print(sum,"it is armstron num")
# else:
#     print(sum, "it is not armstrong num")

num=int(input("enter the num="))
i=0
sum=0
b=num
while i<num:
    rem=num%10
    var=rem**3
    sum=sum+var
    num=num//10
print(sum)
if sum==b:
    print(sum,"it is armstron num")
else:
    print(sum, "it is not armstrong num")
        

   
