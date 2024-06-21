'''
    ip:5
    op: _ _ _ _ a _ _ _ _
        _ _ _ a b a _ _ _
        _ _ a b c b a _ _
        _ a b c d c b a _
'''
n=int(input("Enter a number:"))
for i in range(n):
    res='a'
    print('_'*(n-i),end='')
    for j in range(i+1):
        print(res,end='')
        res=chr(ord(res)+1)
    res=chr(ord(res)-2)
    for j in range(i):
        print(res,end='')
        res=chr(ord(res)-1)
    print('_'*(n-i))