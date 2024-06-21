l=list(map(int,input("Enter the heights of the buildings:").split()))
c1,c2=0,0
for i in range(len(l)-1):
    if l[i+1]>l[i]:
        c1+=1
for i in range(len(l)-1,0,-1):
    if l[i-1]>l[i]:
        c2+=1
print(c1,c2)