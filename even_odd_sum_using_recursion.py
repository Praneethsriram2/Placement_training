def add(l1,a,s1):
    if l1==len(a):
        return s1
    if a[l1]%2==0:
        s1+=a[l1]
    l1+=1
    return add(l1,a,s1)
def add2(l2,b,s2):
    if l2==len(b):
        return s2
    if b[l2]%2!=0:
        s2+=b[l2]
    l2+=1
    return add2(l2,b,s2)
a=list(map(int,input("Enter the elements:").split()))
b=list(map(int,input("Enter the elements:").split()))
l1=0
l2=0
res1=add(l1,a,0)
res2=add2(l2,b,0)
print(res1,res2)      