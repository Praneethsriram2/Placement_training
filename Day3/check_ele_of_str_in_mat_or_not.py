n=int(input("Enter the size of matrix:"))
m=[]
print("Enter the elements:")
for i in range(n):
    m.append(list(map(str,input().split())))
s=input("Enter a string:")
i=0
j=0
flag=1
while i<len(s):
    if s[i] in m[j]:
        m[j].remove(s[i])
        i+=1
        j+=1
        if j==len(m):
            j=0
    else:
        flag=0
        break
if flag==1:
    print("Yes")
else:
    print("No")