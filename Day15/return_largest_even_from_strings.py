s1=input("Enter a string:")
s2=input("Enter another string:")
s=[]
for i in s1:
    if '0'<=i<='9' and i not in s:
        s.append(i)
for i in s2:
    if '0'<=i<='9' and i not in s:
        s.append(i)
for i in range(len(s)):
    s[i]=int(s[i])
s.sort(reverse=True)
if s[-1]%2!=0:
    i=len(s)-2
    while i>=0:
        if s[i]%2==0:
            s[-1],s[i]=s[i],s[-1]
            break
        i+=1
res=''
for i in s:
    res+=str(i)
print(res)