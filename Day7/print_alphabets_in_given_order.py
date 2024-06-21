s=input("Enter the alphabets:")
n=input("Enter the input:")
d=dict()
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in s:
    if i in d:
        print(i*d[i],end='')