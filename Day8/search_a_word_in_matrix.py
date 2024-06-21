'''
4
tued
fwow
roer
drui
    
word
'''
def word(a,i,j,w,k):
    if k==len(w):
        return True
    if i<0 or i>len(a)-1 or j<0 or j>len(a[i])-1 or a[i][j]!=w[k]:
        return False
    a[i]=a[i][:j]+'@'+a[i][(j+1):]
    if word(a,i,j-1,w,k+1) or word(a,i,j+1,w,k+1) or word(a,i-1,j,w,k+1) or word(a,i+1,j,w,k+1):
        return True
    else:
        return False
n=int(input("Enter the size of matrix:"))
a=[]
print("Enter the matrix elements:")
for i in range(n):
    a.append(input())
w=input("Enter a word:")
flag=False
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]==w[0]:
            if word(a,i,j,w,0):
                flag=True
                break
print(flag)