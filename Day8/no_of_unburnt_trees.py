'''
    ip:-
    6->size of the matrix
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0 
    0 0 0 1 1 1
    1 1 0 0 0 1
    1 1 1 0 1 0
    4 6
    that means ath row 6th column tree will catch the fire that will spread the fire top, bottom, left, right. Finally print number of trees unburned
    1's -> trees
    0's -> barlands
    op:-8
'''
def fire(a,i,j):
    if i<0 or i>len(a)-1 or j<0 or j>len(a[i])-1 or a[i][j]==0:
        return
    a[i][j]=0
    fire(a,i,j-1)
    fire(a,i,j+1)
    fire(a,i-1,j)
    fire(a,i+1,j)
n=int(input("Enter the size of matrix:"))
a=[]
print("Enter the elements:")
for i in range(n):
    a.append(list(map(int,input().split())))
fire(a,3,5)
c=0
for i in a:
    for j in i:
        if j==1:
            c+=1
print(f"Total no.of unburnt trees are:{c}")