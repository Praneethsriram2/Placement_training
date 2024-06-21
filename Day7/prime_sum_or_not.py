n=int(input("Enter a number:"))
def prime(i,l):
    if l<=1:
        return False
    if i==(l//2)+1:
        return True
    if l%i==0:
        return False
    return prime(i+1,l)
s=[]
for i in range(1,n+1):
    if prime(2,i):
        s.append(i)
print(s)
flag=0
res=[]
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]+s[j]==n:
            res.append([s[i],s[j]])
            flag=1
            break
    if flag==1:
        break
if flag==1:
    print(res)
    print(True)
else:
    print(False)