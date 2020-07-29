import sys
M, N, K = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10000)
def DFS(g,visited):
    answer =0
    def DFS_visited(g,i,j):
        if g[i][j]==0 and visited[i][j] == False and i <=M-1 and j<=N-1:
            visited[i][j] = True
            nonlocal answer
            answer +=1

            if i < M-1 and g[i+1][j] == 0 : DFS_visited(g, i+1, j)
            if i > 0 and g[i-1][j] == 0 : DFS_visited(g, i-1, j)
            if j < N-1 and g[i][j+1] == 0: DFS_visited(g, i, j+1)
            if j > 0 and g[i][j-1] == 0 : DFS_visited(g, i, j-1)

    DFS_visited(g,i,j)
    return answer, visited

g = [[0 for i in range(N)] for i in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

for i in range(K):
    l_x, l_y, r_x, r_y = map(int ,sys.stdin.readline().split())

    for j in range(l_x,r_x):
        for i in range(l_y, r_y):
            if g[i][j] ==0:
                g[i][j]= 1
            else:
                pass

answer=[]

for i in range(M):
    for j in range(N):
        if visited[i][j] == False and g[i][j]==0:
            num, visited = DFS(g,visited)
            answer.append(num)

answer.sort()

print(len(answer))
for i in answer:
    print(i)

