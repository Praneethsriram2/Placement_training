"""
ip:-
    take input of the string
    abfgresagtyuiofde
op:-
    print longest sub string without repeating character
    12 resagtyuiofd
"""
'''
s=input("Enter a string:")
c1,c2=0,0
d=dict()
i,j=0,0
while j<len(s):
    if s[j] not in d:
        d[s[j]]=1
        j+=1
    else:
        i+=1
        j=i
        c1=len(d)
        d=dict()
    c1=len(d)
    if c1>c2:
        c2=c1
print(c2) '''
s=input("Enter a string:")
d=dict()
d[s[0]]=0
mx=-1
j=0
n=len(s)
i=1
while i<n:
    if s[i] not in d:
        d[s[i]]=i
    else:
        if mx<i-j:
            mx=i-j
        if d[s[i]]>j:
            j=d[s[i]]+1
        d[s[i]]=i
    i+=1
if mx<(i-j):
    mx=i-j
print(mx)