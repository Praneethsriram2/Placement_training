def password(pwd):
    flag1,flag2,flag3,flag4,flag5=1,1,1,1,1
    c=0
    length=0
    if len(pwd)<8:
        length=8-len(pwd)
    elif len(pwd)>=8:
        flag1=-1
    for i in pwd:
        if ('a'<=i<='z'):
            flag2=0
        if ('A'<=i<='Z'):
            flag3=0
        if ('0'<=i<='9'):
            flag4=0
        if i in '!@#$%^&*()-_+=<>?/\\':
            flag5=0
    if flag2==1:
        c+=1
    if flag3==1:
        c+=1
    if flag4==1:
        c+=1
    if flag5==1:
        c+=1
    if flag1==-1 and flag2==0 and flag3==0 and flag4==0 and flag5==0:   
        print("All satisfied",-1)
    elif length>c:
        print(length)
    else:
        print(c) #Print the greater from 'length' and 'c'...
pwd=input("Enter the password:")
password(pwd)