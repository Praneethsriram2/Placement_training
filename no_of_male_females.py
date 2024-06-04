#Brute force...
def male_fem(s):
    c=0
    for i in s:
        if i=='M':
            c+=1
        else:
            c-=1
    if c==0:
        return 0
    elif c>1:
        return 'M'
    else:
        return 'F'
s=input("Enter the input:")
print(male_fem(s))

