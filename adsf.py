N=int(input())
tree ={i+1:[] for i in range(N)}
visited =[True] +[False for i in range(N)]
for i in range(N-1):
    p,c,w = map(int, input().split())
    tree[p].append((c,w))
    tree[c].append((p,w))

def farrestNode(tree, node):
    q=[(i[0], i[1], 0) for i in tree[node]]
    visited = [True] + [False for i in range(N)]
    MAX=0
    MAX_idx=0
    visited[node] = True
    while(q):
        c, w, dist = q.pop()
        if visited[c] == False:
            visited[c] =True
            if dist + w > MAX:
                MAX = dist+w
                MAX_idx = c
            for i in tree[c]:
                    q.append((i[0],i[1],dist+w))

    return MAX, MAX_idx

fdistance, fnode = farrestNode(tree,1)
sDistance, snode = farrestNode(tree,fnode)
print(sDistance)









