import sys
w, h = map(int, sys.stdin.readline().split())
g =[list(map(int, sys.stdin.readline().split())) for _ in range(h)]
visited= [[False for i in range(w)] for i in range(h)]
cnt =0
#1 : matured tomato 0: unmatured tomato -1: No tomato
# End Condition : when there is no 0 in g

def finduntomato(g):
    for row in g:
        for col in row:
            if col == 0:
                return False

    return True

def DFS(g,visited,i,j):
    def rDFS(i, j):
        if g[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True

            if g[i+1][j] == 0 and i<h:
                g[i+1][j] = 1
                rDFS(i+1,j)
            if g[i-1][j] == 0 and i>0:
                g[i-1][j] = 1
                rDFS(i-1,j)
            if g[i][j+1] == 0 and j<w:
                g[i][j+1] = 1
                rDFS(i,j+1)
            if g[i][j-1] == 0 and j>0:
                g[i][j-1] = 1
                rDFS(i,j-1)

    rDFS(i,j)



while(finduntomato((g))):
    for i, row in enumerate(g):
        for j, col in enumerate(row):
            if col == 1 and visited[i][j] == False:
                DFS(g,visited,i,j)

    cnt += 1








t=0


while(t<8):
    for i in range(h):
        for j in range(w):
            if g[i][j] == 1:
                if i > 0 and g[i - 1][j] == 0 : g[i - 1][j] = 1
                if i < h-1 and g[i + 1][j] == 0 : g[i + 1][j] = 1
                if j > 0 and g[i][j - 1] == 0 : g[i][j - 1] = 1
                if j < w-1 and g[i][j + 1] == 0 : g[i][j + 1] = 1

    for i in range(h):
       if 0 in i:
           t += 1





# def looktomato(w,h,g):
#     cnt =0
#     for i in range(h):
#         for j in range(w):
#             if g[i][j]==1:
#                 cnt +=1
#                 bematured(g,i,j)

