num=int(input("enter the num"))
i=1
sum=0
# a=num
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
print(sum)
if sum==num:
    print(sum,"it is perfect num")
else:
    print(sum,"it is not perfect num")

