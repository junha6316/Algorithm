import sys
from collections import deque
N=int(input())
tree ={i+1 :[] for i in range(N)}
check=[True]+[False for i in range(N)]
for i in range(N-1):
    p, c, w=map(int, sys.stdin.readline().split())
    tree[p].append((c,w))
    tree[c].append((p,w))

def bfs(num):
    node, dist =0,0
    q=deque()
    q.append((num,0))
    while q:
        now, now_dist= q.popleft()
        for child in tree[now]:
            if not check[child[0]]:
                check[child[0]] =True
                q.append((child[0],now_dist+child[1]))

                if dist < now_dist+child[1]:
                    dist = now_dist+child[1]
                    node = child[0]
    return dist, node

def init():
    for i in range(len(check)):
        check[i]= False

dist, node = bfs(1)
check=[True]+[False for i in range(N)]

dist, node = bfs(node)
print(dist)
