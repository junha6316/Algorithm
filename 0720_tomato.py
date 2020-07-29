def BFS(g, ripe):
    dx =[1,-1,0,0]
    dy =[0,0,1,-1]
    N= len(g)
    M= len(g[0])
    answer =0
    while(ripe):
        for _ in range(len(ripe)):
            x, y = ripe.popleft()
            for i in range(4):
                nx = x +dx[i]
                ny = y +dy[i]
                if 0<= nx < N and 0<=ny< M and g[nx][ny] ==0:
                    g[nx][ny] =g[x][y]+1
                    ripe.append([nx,ny])
        answer +=1

    for b in g:
        if 0 in b:
            return -1

    return answer -1

from collections import deque
M, N = map(int, input().split())
g = [list(map(int, input().split())) for i in range(N)]
ripe=deque()

for i in range(N):
    for j in range(M):
        if g[i][j] == 1:
            ripe.append((i,j))

print(BFS(g, ripe))





