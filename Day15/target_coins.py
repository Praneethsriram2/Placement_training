def coins(l,target):
    if target==0:
        return True
    if target<0 or not l:
        return False
    return coins(l[1:],target) or coins(l[1:],target-l[0])
l=list(map(int,input("Enter the elements:").split()))
target=int(input("Enter the target:"))
print(coins(l,target))