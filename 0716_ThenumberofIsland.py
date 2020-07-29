import sys
sys.setrecursionlimit(100000)
while(True):
    w,h = map(int, sys.stdin.readline().split())
    if w==0 and h ==0:
        break
    g=[list(map(int, sys.stdin.readline().split())) for i in range(h)]
    visited =[[False for _ in range(w)] for _ in range(h)]

    def DFS(g,visited,i,j):
        R= len(g)
        C= len(g[0])
        def rDFS(g,i,j):
            if g[i][j] ==1 and visited[i][j]==False:
                visited[i][j] =True

                if i <R-1 and g[i+1][j] == 1: rDFS(g,i+1,j)
                if i >0 and g[i-1][j] == 1: rDFS(g,i-1,j)
                if j <C-1 and g[i][j+1] == 1: rDFS(g,i,j+1)
                if j >0 and g[i][j-1] == 1: rDFS(g,i,j-1)

                if i<R-1 and j <C-1 and  g[i + 1][j+1] == 1: rDFS(g,i+1,j+1)
                if i>0 and j <C-1 and  g[i - 1][j+1] == 1: rDFS(g,i-1,j+1)
                if i >0 and j>0 and g[i-1][j - 1] == 1: rDFS(g,i-1,j-1)
                if i <R-1 and j>0 and g[i+1][j - 1] == 1: rDFS(g,i+1,j-1)

        rDFS(g,i,j)

        return

    answer =0
    for i in range(h):
        for j in range(w):
            if g[i][j] ==1 and visited[i][j] == False:
                DFS(g,visited,i,j)
                answer +=1


    print(answer)
