'''
s=input("Enter a string:")
a=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        a.append(s[i:j])
mx=-9999
res=''
for i in a:
    if i==i[::-1]:
        if len(i)>mx:
            mx=len(i)
            res=i
print(res)'''
s=input("Enter a string:")
mx=-9999
res=''
for  i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if s[i:j]==s[i:j][::-1]:
            if len(s[i:j])>mx:
                mx=len(s[i:j])
                res=s[i:j]
print(res)