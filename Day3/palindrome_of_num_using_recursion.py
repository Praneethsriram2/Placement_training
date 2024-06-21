def revers(n,l):
    if n<=0:
        return l
    rem=n%10
    l=(l*10)+rem
    n=n//10
    return revers(n,l)
n=int(input("Enter a number:"))
l=0
res=revers(n,l)
if res==n:
    print("Palindrome")
else:
    print("Not a palindrome")