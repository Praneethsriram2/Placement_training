'''
    ip:5
    op: * * * * *
        * 1 2 3 *
        * 3 4 5 *
        * 6 7 8 *
        * * * * *
'''
n=int(input("Enter a number:"))
num=1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            print("*",end=' ')
        elif j==0 or j==n-1:
            print("*",end=' ')
        else:
            print(num,end=' ')
            num=num+1
    print()    