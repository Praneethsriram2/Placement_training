n=int(input("Enter a number:"))
k=int(input("Enter the key:"))
if k==1:
    print(n)
else:
    c=1
    for i in range((n//2)+1,-1,-1):
        if n%i==0:
            c+=1
        if k-c==0:
            print(f"{k}th largest factor of {n} is {i}")
            break