s=input("Enter a string:")
c1,c2=0,0
k=[s[0],]
j=1
while j<len(s):
    if s[j] not in k and abs(ord(s[j-1])-ord(s[j]))==1:
        k.append(s[j])
        j+=1
    else:
        c1=len(k)
        k.clear()
        k.append(s[j])
        j+=1
    c1=len(k)
    if c1>c2:
        c2=c1
print(c2)