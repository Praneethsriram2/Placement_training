'''
    ip:-
    take list from user, that contains duplicated values.
    ip1:- 2 2 3 1 1 1 4 2 3 5

    ip2:- 1 2 3 4 1 2 3 1 2

    ip3:- 2 3 1 3 4 3 2
    op:-
    return a 2d list such that each row should not contain duplicate values
    op1:- [2 3 1 4 5
           2 1 3
           1 2
           1]

    op2:- [1 2 3 4
           1 2 3
           1 2]
        
    op3:- [2 3 1 4
           3 2
           3]	
'''
l=list(map(int,input("Enter the elements:").split()))
s=dict()
k=[]
i,j=0,0
while i<len(l):
    dup=[]
    j=i
    while j<len(l):
        if l[j] not in s and l[j]!='@':
            s[l[j]]=1
            l[j]='@'
        if l[j] in s:
            dup.append(j)
        j+=1
    a=list(s)
    k.append(a)
    if dup:
        i=dup[0]
    else:
        break
    s.clear()
for i in k:
    print(i)