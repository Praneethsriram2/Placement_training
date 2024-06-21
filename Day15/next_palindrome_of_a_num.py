n=int(input("Enter a number:"))
def revers(n,res):
    if n%10==n:
        return (res*10)+n
    rem=n%10
    res=res*10+rem
    return revers(n//10,res)
while True:
    ans=revers(n,0)
    if n!=ans:
        n+=1
        ans=revers(n,0)
    else:
        print(n)
        break
    