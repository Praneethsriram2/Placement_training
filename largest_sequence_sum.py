'''
    ip=4 5 6 1 2 3 4 8 9 10 11 12
    op=38 from 8 9 10 11 12
'''
def longest_sequence_sum(a):
    if len(a)==0:
        return
    s=0
    i=0
    mx=-9999
    while(i<len(a)-1):
        if a[i+1]-a[i]==1:
            s+=a[i]
            i+=1
        elif a[i+1]-a[i]!=1:
            s+=a[i]
            if s>mx:
                mx=s
            i+=1
            s=0
        if s>mx:
            mx=s
    print(mx)
a=list(map(int,input("Enter the elements:").split()))
longest_sequence_sum(a)