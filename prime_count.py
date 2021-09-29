num=int(input("enter the num="))
i=2
count_prime=0
while i<num:
    b=2
    while b<i:
        if i%b==0:
            print(i,"it is not prime num")
            break
        b=b+1
    else:
        print(i,"it is prime num")
        count_prime=count_prime+1
    i=i+1
print(count_prime)



# num=int(input("enter the num"))
# i=1
# count=0
# while i<num:
#    if i%2==0:
#         print(i,"it is not prime num")
#         count=count+1
#     else:
#         print(i,"it is prime num")
#     i=i+1
# print(count)