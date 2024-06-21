n1=int(input("Enter a number:"))
n2=int(input("Enter another number:"))
'''
s1=[]
s2=[]
for i in range(min()):
    if n1%i==0:
        s1.append(i)
for i in range(1,(n2//2)+1):
    if n2%i==0:
        s2.append(i)
flag=1
for i in s1:
    if i!=1 and i in s2:
        flag=0
if flag==1:
    print("Co-primes")
else:
    print("Not co-primes")'''
flag=1
for i in range(min(n1,n2)//2,1,-1):
    if n1%i==0 and n2%i==0:
        flag=0
        break
if flag==1:
    print("Co-primes")
else:
    print("Not co-primes")

import math
a=4
b=5
if math.gcd(a,b)==1:
    print("Yes")
else:
    print("No")