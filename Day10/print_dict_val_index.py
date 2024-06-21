s=input("Enter the input:").split(',')
d=dict()
for i in s:
    d[i.split(':')[0]]=i.split(':')[1]
print(d)
res=''
for i in d:
    if str(len(i)) in d[i]:
        res+=i[-1]
    elif str(len(i)) not in d[i]:
        flag=0
        for k in range(len(i)-1,0,-1):
            if str(k) in d[i]:
                res+=i[k-1]
                flag=1
                break
        if flag==0:
            res+='x'
print(res)