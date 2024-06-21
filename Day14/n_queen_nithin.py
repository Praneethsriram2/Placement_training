"""
N-Queen along with an obstacle like knight (Guram)
"""
def top_left_diagonal(i,j,n,b):
    if i<0 or j<0 or i>=n or j>=n:
        return True
    elif b[i][j]=='Q':
        return False
    return top_left_diagonal(i-1,j-1,n,b)
def top_right_diagonal(i,j,n,b):
    if i<0 or j<0 or i>=n or j>=n:
        return True
    elif b[i][j]=='Q':
        return False
    return top_right_diagonal(i-1,j+1,n,b)
def bottom_left_diagonal(i,j,n,b):
    if i<0 or j<0 or i>=n or j>=n:
        return True
    elif b[i][j]=='Q':
        return False
    return bottom_left_diagonal(i+1,j-1,n,b)
def bottom_right_diagonal(i,j,n,b):
    if i<0 or j<0 or i>=n or j>=n:
        return True
    elif b[i][j]=='Q':
        return False
    return bottom_right_diagonal(i+1,j+1,n,b)
def left_row(i,j,n,b):
    if j<0:
        return True
    elif b[i][j]=='Q':
        return False
    return left_row(i,j-1,n,b)
def right_row(i,j,n,b):
    if j>=n:
        return True
    elif b[i][j]=='Q':
        return False
    return right_row(i,j+1,n,b)
def top_col(i,j,n,b):
    if i<0:
        return True
    elif b[i][j]=='Q':
        return False
    return top_col(i-1,j,n,b)
def bottom_col(i,j,n,b):
    if i>=n:
        return True
    elif b[i][j]=='Q':
        return False
    return bottom_col(i+1,j,n,b)

def backtrack(i,j,n,b):
    if j==n:
        return False
    if (i>=n):
        return True
    ok=True
    if b[i][j]!='X' and top_left_diagonal(i,j,n,b) and top_right_diagonal(i,j,n,b) and bottom_left_diagonal(i,j,n,b) and bottom_right_diagonal(i,j,n,b) and left_row(i,j,n,b) and right_row(i,j,n,b) and top_col(i,j,n,b) and bottom_col(i,j,n,b):
        b[i][j]='Q'
        ok=backtrack(i+1,0,n,b)
    else:
        return backtrack(i,j+1,n,b)
    if ok==False:
        b[i][j]='-'
        return backtrack(i,j+1,n,b)
def knight_pos(i,j,n):
    if i-1>=0 and j-2>=0:
        board[i-1][j-2]='X'
    if i+1<n and j-2>=0:
        board[i+1][j-2]='X'
    if i-1>=0 and j+2<n:
        board[i-1][j+2]='X'
    if i+1<n and j+2<n:
        board[i+1][j+2]='X'
    if i-2>=0 and j-1>=0:
        board[i-2][j-1]='X'
    if i-2>=0 and j+1<n:
        board[i-2][j+1]='X'
    if i+2<n and j-1>=0:
        board[i+2][j-1]='X'
    if i+2<n and j+1<n:
        board[i+2][j+1]='X'

n=int(input())
board=[['-'for i in range(n)]for j in range(n)]
print("Knight Position:- ",end='')
r,c=map(int,input().split())
board[r][c]='X'
knight_pos(r,c,n)
"""for i in range(n):
    b=board.copy()
    print(i)
    if backtrack(0,i,n,b):
        board=b
        break"""

backtrack(0,0,n,board)
for i in board:
    print(i)