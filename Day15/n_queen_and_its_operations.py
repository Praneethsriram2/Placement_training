def n_queen(i,j):
    if i==len(board):
        return True
    if j==len(board[i]):
        return False
    if board[i][j]!='x' and board[i][j]!='R' and safe(i,j):
        board[i][j]='Q'
        if n_queen(i+1,0):
            return True
        board[i][j]='0'
    return n_queen(i,j+1)
def safe(i,j):
    for row in range(i):
        if board[row][j]=='Q':
            return False
    row,col=i,j
    while row>=0 and col>=0:
        if board[row][col]=='Q':
            return False
        row-=1
        col-=1
    row,col=i,j
    while row>=0 and col<len(board[i]):
        if board[row][col]=='Q':
            return False
        row-=1
        col+=1
    return True
def knight(i,j):
    board[i][j]='x'
    if i-1>=0 and j-2>=0:
        board[i-1][j-2]='x'
    if i-1>=0 and j+2<len(board[i]):
        board[i-1][j+2]='x'
    if i+1<len(board) and j-2>=0:
        board[i+1][j-2]='x'
    if i+1<len(board) and j+2<len(board[i]):
        board[i+1][j+2]='x'
    if i-2>=0 and j-1>=0:
        board[i-2][j-1]='x'
    if i-2>=0 and j+1<len(board[i]):
        board[i-2][j+1]='x'
    if i+2<len(board) and j-1>=0:
        board[i+2][j-1]='x'
    if i+2<len(board) and j+1<len(board[i]):
        board[i+2][j+1]='x'
def rook(i,j):    
    board[i][j]='R'
    temp=i
    while temp>=0:
        board[temp][j]='R'
        temp-=1
    temp=i
    while temp<len(board):
        board[temp][j]='R'
        temp+=1
    temp=j
    while temp>=0:
        board[i][temp]='R'
        temp-=1
    temp=j
    while temp<len(board[i]):
        board[i][temp]='R'
        temp+=1
n=int(input("Enter the size of matrix:"))
board=[['0' for i in range(n)]for j in range(n)]
for i in board:
    print(i)
n_queen(0,0)
a=list(map(int,input("Enter the position to place knight:").split()))
knight(a[0],a[1])
r=list(map(int,input("Enter the position to place rook:").split()))
rook(r[0],r[1])
print("Board after inserting queens are:")
for i in board:
    print(i)