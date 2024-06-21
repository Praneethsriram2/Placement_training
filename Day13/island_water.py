def island(m,i,j,res):
    if i<0 or i>len(m)-1 or j<0 or j>len(m[i])-1 or m[i][j]==0:
        return 0
    m[i][j]=0
    res=1
    a=island(m,i+1,j,res)
    b=island(m,i-1,j,res)
    c=island(m,i,j+1,res)
    d=island(m,i,j-1,res)
    return res+a+b+c+d
n=int(input("Enter the size of matrix:"))
m=[]
print("Enter the elements:")
for i in range(n):
    m.append(list(map(int,input().split())))
c=0
mx=0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]==1:
            area=island(m,i,j,0)
            c+=1
            if area>mx:
                mx=area
print(c,mx)