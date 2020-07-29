import sys
N=int(sys.stdin.readline())
g = [list(map(int, sys.stdin.readline().split())) for i in range(N)]


def DFS(g,s):
    visited = [False for i in range(N)]
    def DFS_visited(visited ,g, i):
        for j in range(N):
            if g[i][j]==1 and visited[j]==False:
                visited[j]=True
                DFS_visited(visited, g, j)

    DFS_visited(visited,g, s)
    for idx, i in enumerate(visited):
        if i == True:
            g[s][idx] =1
    return g

for i in range(N):
    DFS(g,i)

for i in range(N):
    for j in range(N):
        g[i][j]= str(g[i][j])

for i in g:
    print(' '.join(i))





'''
first don't visit itself
if g[i][j] ==1:
Do DFS
search and fill row line with 1 and 0 
'''
