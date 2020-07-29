import sys

N= int(sys.stdin.readline())

def cabbage(g,visited, col, row):
    n_r =len(g)
    n_c = len(g[0])
    def DFS(g, visited, col, row):
        if col< len(g) and row<len(g[0]) and visited[col][row]==False:
            if g[col][row] == 1 :
                visited[col][row] = True

            if col< n_r-1 and g[col+1][row] ==1:
                DFS(g, visited, col + 1, row)
            if row< n_c-1 and g[col][row+1] ==1:
                DFS(g, visited, col, row+1)
            if col >=1  and g[col-1][row] ==1:
                DFS(g, visited, col -1, row)
            if row>= 1 and g[col][row-1] ==1:
                DFS(g, visited, col, row-1)

    DFS(g,visited,col,row)

    return visited
answer_li=[]
for i in range(N):
    row, col, nl = map(int, sys.stdin.readline().split())
    g=[[0 for i in range(row)] for _ in range(col) ]
    visited = [[False for i in range(row)] for j in range(col)]
    answer =0

    for i in range(nl):
        x, y =map(int, sys.stdin.readline().split())
        g[y][x] =1

    for i in range(col):
        for j in range(row):
            if g[i][j] == 1 and visited[i][j] ==False:
                visited = cabbage(g, visited, i, j)
                answer += 1
    answer_li.append(answer)

for num in answer_li:
    print(num)


