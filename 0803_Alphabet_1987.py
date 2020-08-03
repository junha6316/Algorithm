
# R, C= map(int, input().split())
#
# board = [' '.join(input()).split() for i in range(R)]
# dx =[1,-1, 0, 0]
# dy =[0, 0,-1,1]
# q=set([(0,0,board[0][0])])
# answer=1
# while q:
#     row, col, word = q.pop()
#     for i in range(4):
#         nrow = row + dx[i]
#         ncol = col + dy[i]
#         if 0<=nrow<R and 0<=ncol<C and board[nrow][ncol] not in word:
#             q.add((nrow,ncol,word + board[nrow][ncol]))
#             answer = max(answer, len(word)+1)
#
#
# print(answer)

R, C= map(int, input().split())

board = [' '.join(input()).split() for i in range(R)]
dx =[1,-1, 0, 0]
dy =[0, 0,-1,1]
q=set([(0,0,board[0][0])])
answer=1
while q:
    row, col, word = q.pop()
    for i in range(4):
        nrow = row + dx[i]
        ncol = col + dy[i]
        if(ny < 0 or nx < 0 or ny >= R or nx >= C):
            continue
        if board[nrow][ncol] in word:
            continue
        else:
            q.add((nrow,ncol,word + board[nrow][ncol]))
            answer = max(answer, len(word)+1)


print(answer)

