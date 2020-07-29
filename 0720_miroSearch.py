from collections import deque
N, M = map(int, input().split())

g = [list(map(int, ' '.join(input()).split())) for i in range(N)]
visit = deque([[0, 0]])
visited = [[False for i in range(M)] for i in range(N)]
visited[0][0]=True
def BFS(g,visit):
    dx =[1,-1,0,0]
    dy =[0,0,1,-1]
    while(visit):
        for i in range(len(visit)):
            x, y = visit.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0<=nx<N and 0<=ny<M and g[nx][ny] ==1 and visited[nx][ny] ==False:
                    g[nx][ny] = g[x][y] +1
                    visit.append([nx,ny])

    return g[-1][-1]
print(BFS(g,visit))




