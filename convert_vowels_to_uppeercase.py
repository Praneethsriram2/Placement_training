l=input("Enter the string:")
res=''
for i in l:
    if i not in "aeiou":
        res+=i
    else:
        i=i.upper()
        res+=i
print(res)