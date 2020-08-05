
from collections import deque
M, N = map(int, input().split())
miro = [list(map(int, ' '.join(input()).split())) for i in range(N)]
visited=[[False for i in range(M)] for i in range(N)]
cost =[[0 for i in range(M)] for j in range(N)]

N-=1
M-=1
answer= []
q= deque()
dx=[1,-1,0,0]
dy=[0,0,-1,1]

q.append((0,0))

MIN=1000

while q:
    row, col =q.popleft()

    if row ==N and col == M:
        MIN = min(MIN, cost[row][col])

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0 <= nx <= N and 0 <= ny <= M and visited[nx][ny] == False:
            if miro[nx][ny] == 0:
                q.appendleft((nx, ny))
                cost[nx][ny] = cost[row][col]
            else:
                q.append((nx, ny))
                cost[nx][ny] = cost[row][col] +1
            visited[nx][ny] = True


print(MIN)



# def dfs(row, col,w):
#     print(row,col)
#     if row ==N and col ==M:
#         answer.append(w)
#         return
#     visited[row][col]=True
#     for i in range(4):
#         nx = row + dx[i]
#         ny = col + dy[i]
#         if 0<=nx<=N and 0<=ny<=M and visited[nx][ny] ==False:
#             if miro[nx][ny] == 0:
#                 dfs(nx,ny,w)
#
# dfs(0,0,0)
# print(answer)
#
# def block():
#






