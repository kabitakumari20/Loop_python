i=1
count_even=0
count_odd=0
while i<=100:
    if i%2==0:
        count_even=count_even+1
    if i%2!=0:
        count_odd=count_odd+1
        count_odd=(count_odd)
    i=i+1
print("count_even",count_even)
print("count_odd",count_odd)