r=int(input("Enter the no.of rows:"))
c=int(input("Enter the no.of columns:"))
s=[[1 for i in range(c)]for j in range(r)]
s[1][3]=0 #->obstacle
def all_paths(i,j,path):
    if i==len(s)-1 and j==len(s[i])-1:
        print(path)
        return 1
    elif i<0 or j<0 or i==len(s) or j==len(s[i]) or s[i][j]==0:
        return 0
    else:
        s[i][j]=0
        path.append((i,j))
        a=all_paths(i,j+1,path)
        b=all_paths(i,j-1,path)
        c=all_paths(i+1,j,path)
        d=all_paths(i-1,j,path)
        s[i][j]=1
        return a+b+c+d
print(all_paths(0,0,[]))