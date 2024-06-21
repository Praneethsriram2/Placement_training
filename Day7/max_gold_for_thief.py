'''
    ip:13 9 4 10 5 7
    op:30 ->13+10+7
    #we shouldn't add elements which are side by side...
'''
l=list(map(int,input("Enter the elements:").split()))
def rec_fun(l,s):
    if not l:
        return s
    return max(rec_fun(l[2:],s+l[0]),rec_fun(l[1:],s))
print(rec_fun(l,0))