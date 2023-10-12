global N
N =4
def print_b(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end="")
        print()
    print()
def is_safe(board,row,col):
    for i in range(col):
        if(board[row][i]==1):
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if(board[i][j]==1):
            return False
    for i,j in zip(range(row,N),range(col,-1,-1)):
        if(board[i][j]==1):
            return False
    return True
def solve(board,col):
    if(col>=N):
        print_b(board)
        print()
        return
    for i in range(N):
        if(is_safe(board,i,col)):
            board[i][col]=1
            solve(board,col+1)
            board[i][col] = 0
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
solve(board,0)
