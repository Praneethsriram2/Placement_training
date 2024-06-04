def even_sum(n,s1):
    if n<=1:
        return s1
    if n%2==0:
        s1+=n
    return even_sum(n-1,s1)
n=int(input("Enter a number:"))
print(even_sum(n,0))