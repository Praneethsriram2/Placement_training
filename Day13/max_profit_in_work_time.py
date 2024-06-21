#It's not correct, check it...
nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
i,k=0,0
j,m=i+1,i+1
res1,res2=0,0
while k<len(nums):
    print(res2)
    if j==len(nums):
        m+=1
        j=m
        res1=0
    if m==len(nums):
        k+=1
        i=k
        j,m=i+1,i+1
    if k==len(nums) and m==len(nums):
        break
    res1+=a[i]
    if nums[j][0]>=nums[i][1]:
        res1+=a[j]
        i=j
    if res1>res2:
        res2=res1
    j+=1
print("Maximum profit is:",res2)