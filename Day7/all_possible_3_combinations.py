'''
l=list(map(int,input("Enter the elements:").split()))
s=[]
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            s.append([l[i],l[j],l[k]])
print(s)'''
'''
def comb(l,i,j,k,s):
    if k==len(l):
        j+=1
        k=j+1
    if j==len(l)-1:
        i+=1
        j=i+1
        k=j+1
    if i>=len(l)-2:
        return s
    s.append([l[i],l[j],l[k]])
    return comb(l,i,j,k+1,s)
l=list(map(int,input("Enter the elements:").split()))
i=0
j=i+1
k=j+1
s=[]
print(comb(l,i,j,k,s))
'''
def comb(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr,end=' ')
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=list(map(int,input("Enter the elements:").split()))
k=3
comb(a,k)