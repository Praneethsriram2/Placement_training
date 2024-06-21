def odd_even(l1,l2,l3,i,j):
    if i==len(l1):
        return l3
    if j==len(l1):
        return odd_even(l1,l2,l3,i+1,0)
    if l1[i]%2==0 and l2[j]%2!=0:
        l3.append(l1[i]+l2[j])
    if l1[i]%2!=0 and l2[j]%2==0:
        l3.append(l1[i]+l2[j])
    return odd_even(l1,l2,l3,i,j+1)
l1=list(map(int,input("Enter the elements:").split()))
l2=list(map(int,input("Enter the elements:").split()))
print(odd_even(l1,l2,[],0,0))
def add_even(l1,l2,l3,i,j,s):
    if i==len(l1):
        return l3
    if j==len(l1):
        l3.append(s)
        return add_even(l1,l2,l3,i+1,0,0)
    if l1[i]%2==0 and l2[j]%2!=0:
        s+=l1[i]+l2[j]
    return add_even(l1,l2,l3,i,j+1,s)
print(add_even(l1,l2,[],0,0,0))