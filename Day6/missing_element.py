n=int(input("Enter a number:"))
l=list(map(int,input("Enter the elements:").split()))
l1=n*(n+1)//2
l2=0
for i in l:
    l2+=i
print("Missing element is:",l1-l2)