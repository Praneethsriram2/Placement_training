'''
    ip=1 2 3 2 3 4 5 1 5
    op=[1:2, 2:2, 3:2, 4:1, 5:2]
'''
def count_numbers(l):
    if len(l)==0:
        return
    d=dict()
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
l=list(map(int,input("Enter th elements:").split()))
count_numbers(l)