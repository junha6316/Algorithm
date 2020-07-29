import sys
N=int(sys.stdin.readline())
sys.setrecursionlimit(10000)
g =[list(map(int, sys.stdin.readline().split())) for i in range(N)]

rain=set([])

for i in g:
    rain.update(i)

ma=max(rain)

def DFS(g, precipitation, visited, N, i, j):

    def DFS_visited(g, precipitation, i, j):
        if (i < N and j < N) and (visited[i][j]==False) and g[i][j] > precipitation:
            visited[i][j] = True

            if i < N - 1 and g[i + 1][j] > precipitation: DFS_visited(g, precipitation, i + 1, j)
            if i > 0 and g[i - 1][j] > precipitation: DFS_visited(g,precipitation, i - 1, j)
            if j < N - 1 and g[i][j + 1] > precipitation: DFS_visited(g, precipitation, i, j + 1)
            if j > 0 and g[i][j - 1] > precipitation: DFS_visited(g,precipitation, i, j - 1)

    DFS_visited(g, precipitation, i, j)

    return visited

answer_li=[]
max=0
for precipitation in range(0,ma+1):
    answer=0
    visited = [[False for i in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if g[i][j] > precipitation and visited[i][j]==False:
                DFS(g, precipitation, visited, N, i, j)
                answer +=1

    if max < answer:
        max =answer

print(max)
