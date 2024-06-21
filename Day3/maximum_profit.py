l=list(map(int,input("Enter the prices:").split()))
mx=0
'''for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]-l[i]>mx:
            mx=l[j]-l[i]'''
'''
i=0
j=i+1
while i<len(l)-1:
    if l[j]-l[i]>mx:
        mx=l[j]-l[i]
        j+=1
    elif l[j]-l[i]<mx:
        j+=1
    if j==len(l):
        i+=1
        j=i+1'''
k=l[0]
for i in range(1,len(l)):
    if (l[i]-k)<0:
        k=l[i]
    if mx<(l[i]-k):
        mx=l[i]-k
print(f"Maximum profit is:{mx}")