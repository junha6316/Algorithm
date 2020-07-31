'''

R, M, A, F, N, T
2*2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임

R, M, A, F, N, T을 기준으로 DFS

'''
board =[
     'AATAA'
    ,'AATAA'
    ,'BAAAA'
    ,'AAAAA']

def solution(N,M,board):
    board =[(' '.join(i)).split() for i in board]
    N = len(board)
    M = len(board[0])

    def CheckTwoByTwo(board, i, j):
        fcon= board[i][j] == board[i+1][j]
        scon= board[i][j] == board[i][j+1]
        tcon= board[i][j] == board[i+1][j+1]
        return fcon and scon and tcon

    answer=0

    t=0
    while(True):
        delete = []

        for i in range(N-1):
            for j in range(M-1):
                if CheckTwoByTwo(board, i, j) and board[i][j] != '':
                    delete.extend([(i,j), (i+1,j), (i,j+1), (i+1,j+1)])

        delete = list(set(delete))

        if len(delete) ==0:break

        for row, col in delete:
            board[row][col] =''
            answer +=1

        for col in range(0,M):
            for row in range(N-1,0,-1):
                if board[row][col] =='' and board[row-1][col] !='':
                    temp = board[row-1][col]
                    board[row-1][col] = board[row][col]
                    board[row][col] = temp

        for col in range(0,M):
            for row in range(N-1,0,-1):
                if board[row][col] == '':
                    i,j = row, col
                    while(row > 0):
                        row -= 1
                        if board[row][col] != '':
                            board[i][j], board[row][col] =  board[row][col], ''
                            break

    return answer





print(solution(board))










