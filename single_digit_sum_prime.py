'''
    ip:538
    op:538
    explantion:5+3+8=16->1+6=7 is prime
    ip:499
    op:500
    explanation:4+9+9=22->2+2=4, so increment 499+1=500->5+0+0=5 is prime
                so output is 500...
'''
def prime(n):
    num=n
    while num>9:
        s=0
        n=num
        while n>0:
            tot=n%10
            s+=tot
            n=n//10
        num=s
    return num
n=int(input("Enter a number:"))
res=0
while True:
    res=prime(n)
    if res==2 or res==3 or res==5 or res==7:
        print(n)
        break
    else:
        n+=1