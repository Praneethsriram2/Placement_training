l=list(map(float,input("Enter the elements:").split()))
s1,s2,s3=0,0,0
for i in l:
    if int(i)==i: #or use i%1==0...
        if i%2==0:
            s1+=i
        elif i%2!=0:
            s2+=i
    else:
        s3+=i
print("Even sum is:",s1,"Odd sum is:",s2,"Float sum is:",s3)