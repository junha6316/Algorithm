import sys
n_node, nl = map(int, sys.stdin.readline()[:-1].split())

visited = [False for i in range(n_node)]
connection = [tuple(map(int, sys.stdin.readline().split())) for i in range(nl)]
g ={i :[] for i in range(1,n_node+1)}

for start, end in connection:
    g[start].append(end)
    if start not in g[end]:
        g[end].append(start)

def DFS(g, visited,start):
    n_node = len(g.keys())

    def DFS_visited (g, visited,start):
        if start <n_node+1 and visited[start-1] == False:
            visited[start-1] = True
            for i in g[start]:
                if visited[i-1]==False:
                    DFS(g, visited, i)
    DFS_visited(g,visited,start)
    return visited

answer =0
for i in range(1,n_node+1):
    if visited[i-1] ==False:
        visited = DFS(g,visited,i)
        answer +=1
print(answer)











