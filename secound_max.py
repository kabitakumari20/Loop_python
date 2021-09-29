a=[1,2,5,6,9,5,]
i=0
max=a[0]
secound_max=a[0]
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
    j=0
    while j<len(a):
        if max>a[j] and secound_max<a[j]:
            secound_max=a[j]
        j=j+1
print(secound_max)
            
    