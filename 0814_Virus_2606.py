N= int(input())
visited =[True] + [False for i in range(N)]
M = int(input())
tree = {i :[] for i in range(1, N+1)}

for i in range(M):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)


def dfs(tree):
    answer= 0
    def rdfs(node):
        for n in tree[node]:
            if not visited[n]:
                nonlocal answer
                answer +=1
                visited[n]=True
                rdfs(n)

    visited[1] =True
    rdfs(1)

    return answer

print(dfs(tree))






