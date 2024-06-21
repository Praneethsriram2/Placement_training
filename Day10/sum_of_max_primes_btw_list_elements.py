n=list(map(int,input("Enter the elements:").split()))
j=0
def prime(k,l):
    if l<=1:
        return False
    if k==(l//2)+1:
        return True
    if l%k==0:
        return False
    return prime(k+1,l)
res=[]
while j<len(n)-1:
    s=[]
    for m in range(n[j],n[j+1]):
        if prime(2,m):
            s.append(m)
    j+=1
    if s:
        res.append(max(s))
print(sum(res))