'''
    in:aaabbbccdddd
    op:a3b3c2d4
'''
s=input("Enter the string:")
i=0
j=1
c=1
while(j<len(s)):
    if s[i]==s[j]:
        c+=1
        i+=1
        j+=1
    elif s[i]!=s[j]:
        print(s[i]+str(c),end=' ')
        i+=1
        j+=1
        c=1
print(s[i]+str(c))