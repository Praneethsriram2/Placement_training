n=list(map(int,input("Enter the elements:").split()))
'''if len(n)&1==0: #or len(n)%2==0
    print("YES")
else:
    print("NO")'''
i=0
j=-1
while id(n[i+1])!=id(n[j]) and id(n[i])!=id(n[j]):
    i+=1
    j-=1
if id(n[i])==id(n[j]):
    print("No")
else:
    print("Yes")