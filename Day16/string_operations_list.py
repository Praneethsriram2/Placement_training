n=int(input("Enter the no.of queries:"))
l=[]
for i in range(n):
    a,b=input("Enter the query:").split()
    if a=='1':
        if b not in l:
            l.append(b)
    elif a=='2':
        if b in l:
            print(True)
        else:
            print(False)
    elif a=='3':
        c=0
        for j in l:
            if b in j:
                c+=1
        print(c)
    elif a=='4':
        l.remove(b)
        print(l)