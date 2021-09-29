i=1
c_e=0
c_odd=0
while i<=9:
    if i%2==0:
        c_e=c_e+1
    if i%2!=0:
        c_odd=c_odd+1
    i=i+1
print(c_e)
print(c_odd)