# from collections import deque
#
# dx=[1,-1,0,0]
# dy = [0,0,1,-1]
# border = deque()
# for i in range(N):
#     for j in range(N):
#         if l[i][j]==1:
#             visited[i][j] = True
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0<=nx<N and 0<=ny<N and l[nx][ny] ==0:
#                     border.append([i,j])
#                     break
#
# def BFS(l,visited,border):
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     while(border):
#         for i in range(len(border)):
#             x,y = border.popleft()
#             for k in range(4):
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if 0 <= nx < N and 0 <= ny < N and l[nx][ny] == 0 and visited[nx][ny] ==False:
#                     visited[nx][ny] =True
#                     l[nx][ny] = l[x][y]+1
#                     border.append([nx, ny])
#     return

# def DFS(l):
#     visited = [[False for i in range(N)] for i in range(N)]
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     def rDFS(i,j):
#         if visited[i][j] == False and l[i][j] != 0:
#             visited[i][j] = True
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0 <= nx < N and 0 <= ny < N and l[nx][ny] == 0 and visited[nx][ny] == False:
#                     l[nx][ny] = l[i][j]+1
#                     rDFS(nx,ny)
#                 if l[nx][ny] == 1 and visited[nx][ny] == False:
#                     rDFS(nx+1,ny)
#     rDFS(0,0)
#     return
#
#
# N= int(input())
# l = [list(map(int, input().split())) for i in range(N)]
# visited =[[False for i in range(N)] for i in range(N)]
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def dfs(l,visited):
#     def rdfs(i,j,n_isl):
#         if visited[i][j] ==False and l[i][j]==1:
#             visited[i][j] = True
#             l[i][j] =n_isl
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0<=nx<N and 0<=ny<N and l[nx][ny] ==1:
#                     rdfs(nx,ny,n_isl)
#     n_isl =1
#     for i in range(N):
#         for j in range(N):
#             if l[i][j] == 1 and visited[i][j] == False:
#                 rdfs(i,j,n_isl)
#                 n_isl+=1
#     return n_isl
# n_isl=dfs(l,visited)
#
#
# from collections import deque
#
# def bfs(l,z):
#     border = deque([])
#     ans = 99999999
#     dist = [[-1] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if l[i][j] == z:
#                  border.append([i, j])
#                  dist[i][j] =0
#
#
#     while(border):
#         x, y = border.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if l[nx][ny] == 0 and dist[nx][ny] ==-1:
#                     dist[nx][ny] = dist[x][y] +1
#                     border.append([nx,ny])
#
#                 if  l[nx][ny] !=0 and l[nx][ny] !=z:
#                     ans = min(ans, dist[x][y])
#                     return ans
#
# ans=9999999
# for i in range(1,n_isl):
#     ans= min(ans,bfs(l,i))
# print(ans)
from collections import deque

N=int(input())
l = [list(map(int, input().split())) for i in range(N)]
visited =[[False for i in range(N)] for i in range(N)]
dx =[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(l):
    n =1
    def rdfs(i,j, n):
        if visited[i][j] ==False:
            l[i][j] = n
            visited[i][j] =True
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<= nx<N and 0<= ny <N and l[nx][ny] !=0 and visited[nx][ny] == False:
                    rdfs(nx,ny,n)

    for i in range(N):
        for j in range(N):
            if visited[i][j] ==False and l[i][j] !=0:
                rdfs(i,j,n)
                n+=1
    return n

n=dfs(l)

def bfs(l,z):
    q= deque([])
    dist =[[-1 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if l[i][j] == z:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and l[nx][ny] == 0:
                        dist[i][j]=0
                        q.append((i,j))
                        break
    ans=9999999
    while(q):
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx <N and 0<= ny <N:
                if l[nx][ny]==0 and dist[nx][ny] ==-1:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))
                if l[nx][ny] !=0 and l[nx][ny] !=z:
                    ans =min(ans, dist[x][y])
                    return ans

    return ans

ans =99999
for i in range(1,n):
    ans =min(ans, bfs(l,i))
print(ans)

























