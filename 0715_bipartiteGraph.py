def dfs(visited):
    def rdfs(i):
        visited[i] = True
        for j in dic[i]:
            if visited[j] == False:
                rdfs(j)

    for i in dic.keys():
        if visited[i] == False:
            rdfs(i)

        if False in visited:
            return "YES"
        else:
            return "NO"

n= int(input())
for i in range(n):
    N, E= map(int, input().split())
    dic ={i+1 :[] for i in range(N)}
    for i in range(E):
        p, c = map(int, input().split())
        dic[p].append(c)

    visited =[True] + [False for i in range(N)]

    print(dfs(visited))








