

#R row C column

import sys
R, C  = map(int, sys.stdin.readline().split())
g=[' '.join(sys.stdin.readline()[:-1]).split() for i in range(R)]
for i in g: print(i)
sys.setrecursionlimit(100000)

def DFS(g,path,i,j):
    answer = 0
    R, C= len(g), len(g[0])
    def rDFS(g,i,j):
        if i<R and j<C and g[i][j] not in path:
            path.append(g[i][j])
            nonlocal answer
            answer += 1

            if i < R - 1 and g[i + 1][j] not in path: rDFS(g, i + 1, j)
            if j < C - 1 and g[i][j + 1] not in path: rDFS(g, i, j + 1)
            if i > 0 and g[i - 1][j] not in path: rDFS(g, i - 1, j)
            if j > 0 and g[i][j - 1] not in path: rDFS(g, i, j - 1)

    rDFS(g, i, j)
    return answer

path = [g[0][0]]
a= DFS(g, path, 0, 1)
path = [g[0][0]]
b= DFS(g, path, 1, 0)
print(max(a,b)+1)






