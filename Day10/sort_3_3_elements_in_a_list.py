l=list(map(int,input("Enter the elements:").split()))
s=[]
i=0
while i<len(l)-2:
    if l[i]<l[i+1] and l[i]<l[i+2]:
        if l[i+1]<l[i+2]:
           l[i],l[i+1],l[i+2]=l[i],l[i+2],l[i+1]
        else:
            l[i],l[i+1],l[i+2]=l[i],l[i+1],l[i+2]
    elif l[i+1]<l[i] and l[i+1]<l[i+2]:
        if l[i]<l[i+2]:
            l[i],l[i+1],l[i+2]=l[i+1],l[i],l[i+2]
        else:
            l[i],l[i+1],l[i+2]=l[i+1],l[i+2],l[i]
    else:
        if l[i]<l[i+1]:
            l[i],l[i+1],l[i+2]=l[i+2],l[i],l[i+1]
        else:
            l[i],l[i+1],l[i+2]=l[i+2],l[i+1],l[i]
    i+=1
print(l)