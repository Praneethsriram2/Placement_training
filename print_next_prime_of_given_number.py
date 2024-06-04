n=int(input("Enter a number:"))
if n==2:
    print(n)
else:
    if n%2==0:
        n+=1 #if it's even convert to odd...
    while True:
        flag=1
        for i in range(2,(n//2)+1): #use half of 'n', because the factors will be present only upto the half of the 'n'(ex:6->check upto 3->n//2)...
            if n%i==0:
                flag=0 
                break #here condition satisfied so i breaked the loop(not a prime) only after 1st iteration...
        if flag==1:
            print(n)
            break
        n+=2 #this takes only odd numbers
#or we can also count the no of factors to find the prime number...
#if count==2 it's prime, else not prime...