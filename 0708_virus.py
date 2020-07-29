

#
# graph=  [[2, 0, 0, 0, 1, 1, 0]
#         ,[0, 0, 1, 0, 1, 2, 0]
#          ,[0, 1, 1, 0, 1, 0, 0]
#          ,[0, 0, 0, 0, 0, 0, 0]
#          ,[0, 1, 0, 0, 0, 1, 1]
#          ,[0, 1, 0, 0, 0, 0, 0]
#          ,[0, 1, 0, 0, 0, 0, 0]]

# row = len(graph)
# col = len(graph[1])

def simulation(g,visited, i ,j):
    n_two=0
    def DFS(g, visited, i ,j):
        n_row = len(g)
        n_col = len(g[0])
        if i < n_row and j < n_col :
            if visited[i][j]==False:
                if g[i][j] ==2 :
                    visited[i][j] = True
                    nonlocal n_two
                    n_two +=1

                    if i >= 1 and g[i-1][j]==0: g[i-1][j]=2
                    if j >= 1 and g[i][j-1]==0: g[i][j-1]=2
                    if i < n_row-1 and g[i+1][j]==0: g[i+1][j]=2
                    if j < n_col-1 and g[i][j+1]==0: g[i][j+1]=2

                if i >= 1 and g[i-1][j]==2:
                    DFS(g, visited, i - 1, j)
                if j >= 1 and g[i][j-1]==2:
                    DFS(g, visited, i, j-1)
                if i < n_row-1 and g[i+1][j]==2:
                    DFS(g, visited, i+1, j)
                if j < n_col-1 and g[i][j+1]==2:
                    DFS(g, visited, i, j + 1)

    DFS(g, visited, i,j)
    return n_two


import sys
import copy

sys.setrecursionlimit(10**8)
row, col= map(int, sys.stdin.readline().split())
graph=[list(map(int, sys.stdin.readline().split())) for _ in range(row)]

coordinate=[]
virus=[]
n_one =0
for i in range(row):
    for j in range(col):
        if graph[i][j]==0:
            coordinate.append([i,j])
        elif graph[i][j] ==1:
            n_one +=1
        elif graph[i][j] ==2:
            virus.append([i,j])


MAX =-1
for i in range(len(coordinate)):
    for j in range(1,len(coordinate)):
        for k in range (2,len(coordinate)):

            visited =[[False for i in range(col)] for i in range(row)]
            g = copy.deepcopy(graph)
            total_n_two=0
            g[coordinate[i][0]][coordinate[i][1]] = 1
            g[coordinate[j][0]][coordinate[j][1]] = 1
            g[coordinate[k][0]][coordinate[k][1]] = 1

            for a,b in virus:
                if visited[a][b] == False:
                    n_two=simulation(g, visited, a, b)
                    total_n_two += n_two

            answer = row*col -(n_one+3)-total_n_two

            if MAX < answer:
                MAX = answer

print(MAX)

'''
1. 0인 곳에 벽을 세울수있다.

DFS를 이용헤 바이러스를 퍼트린
전체 개수 -1의 개수 +3 + 2의 개수 => 안전영역ㅢ 크
벽을 세운 후에 시뮬레이션을 통해 안전영역의 크기를 구한다. 
'''

