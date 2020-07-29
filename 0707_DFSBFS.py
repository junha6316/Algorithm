import sys
N, nl, st =map(int, sys.stdin.readline().split())
graph={i:[] for i in range(N)}

for i in range(nl):
    I=tuple(map(int, sys.stdin.readline().split()))
    for i in I:
        if i not in graph.keys():
            graph[i] =[]

    graph[I[0]].append(I[1])

    if I[0] not in graph[I[1]]:
        graph[I[1]].append(I[0])

    graph[I[0]].sort()


def DFS(graph, s):
    visited=[]
    def DFS_visited(graph, visted, s):
        visted.append(s)
        for i in graph[s]:
            if i not in visted:
                DFS_visited(graph, visited, i)

    DFS_visited(graph, visited, s)

    a = ''
    for i in visited:
        a += str(i) + ' '
    print(a[:-1])

    return

from collections import deque
def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    a = ''
    for i in visited:
        a += str(i) + ' '
    print(a[:-1])




DFS(graph, st)
BFS(graph, st)















