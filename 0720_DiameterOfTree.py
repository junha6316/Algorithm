# N=int(input())
# visited=[True] +[False for i in range(N)]
# tree={i+1:[] for i in range(N)}
# for i in range(N):
#     a = list(map(int, input().split()))
#     for i in range(1,len(a)-1):
#
#
#         if i %2 ==1:
#             if (a[0],a[i+1]) in tree[a[1]]: pass
#             else:
#                 tree[a[0]].append((a[i],a[i+1]))
#
#
# print(tree)
#
#
#
# def bfs(Tree,visited):
#     while(visited):
#         for i in range(len(visited)):
#             for
#
# print(dfs(tree))
#
# from collections import deque
# def bfs(num):
#     dist, num = 0,0
#     q = deque()
#     q.append((num, 0))
#     check[num]= True



from collections import deque
import sys


def bfs(num):
    dist, node =0,0
    q = deque()
    q.append((num,0))
    check[num]=True
    while q:
        now, now_dist = q.popleft()
        for i in adj[now]:
            if check[i[0]] == False:
                check[i[0]] =True
                q.append((i[0],i[1]+now_dist))

                if now_dist + i[1] > dist:
                    dist = now_dist +i[1]
                    node =i[0]
    return dist, node

n = int(sys.stdin.readline())
check= [False for i in range(n)]
adj = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(temp) - 1, 2):
        adj[temp[0] - 1].append((temp[j] - 1, temp[j + 1]))
for i in adj:
    print(adj)
def init():
    for i in range(n):
        check[i] = False

dist, node = bfs(1)
init()
dist, node = bfs(node)
print(dist)


import sys
sys.setrecursionlimit(10**5)
N= int(input())
check =[True]+[False for i in range(N)]
def fahrest(num):
    node,dist =0,0
    q =deque()
    q.append((num,dist))
    while(q):
        now, now_dist = q.popleft()
        for i in adj[now]:
            if not check[i[0]]:
                check[now] =True
                q.append((i[0], i[1]+now_dist))

                if now_dist+i[1] >dist:
                    dist = now_dist +i[1]
                    node = i[0]
    return dist, node

