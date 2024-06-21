'''
    ip:4 4 1 2 4 7 4
    op:4
    ip:1 1 2 2 3 2
    op:2
    #Element should repeat atleast half of len of the list...
'''
l=list(map(int,input("Enter the elements:").split()))
'''d=dict()
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
flag=0
for i in d:
    if d[i]>=len(l)//2:
        flag=1
        print(i)
if flag==0:
    print("No element found for the conditions")'''
#The below code takes the o(1) space complexity and 0(n) time complexity...
c=1
w=l[0]
for i in range(1,len(l)):
    if l[i-1]==l[i]:
        c+=1
    else:
        c-=1
    if c==0:
        c=1
        w=l[i]
print(w)