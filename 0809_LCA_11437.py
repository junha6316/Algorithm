import sys
def LCA(a,b):
    if an[a][0]>an[b][0]:
        a = an[a][1]
        LCA(a,b)

    elif an[a][0]<an[b][0]:
        b = an[b][1]
        LCA(a, b)

    else:
        if a==b:
            print(a)
        else:
            while an[a][1] != an[b][1]:
                a= an[a][1]
                b= an[b][1]

            print(an[a][1])


N= int(sys.stdin.readline())
dic ={i:[] for i in range(1, N+1)}
visited =[True, True]+[False for i in range(1,N)]
an =[[0 for i in range(N+1)] for i in range(21)]
# an[1] =(0,1)
for i in range(1,N):
    n1, n2 = map(int, sys.stdin.readline().split())
    dic[n1].append(n2)
    dic[n2].append(n1)
q=[]
q.append((1,1)) #(depth, N_node)

while(q):
    depth, node=q.pop(0)
    for ch in dic[node]:
        if visited[ch] == False:
            visited[ch] = True
            q.append((depth+1, ch))
            an[depth][ch] = node

for i in an:
    print(i)


# m = int(sys.stdin.readline())
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     LCA(a,b)


LCA(1,1)

# import sys
#
#
# N= int(sys.stdin.readline())
# p_list = [0 for _ in range(N+1)]
# for _ in range(N-1):
#     p, c = map(int, sys.stdin.readline().split())
#     p_list[c] =p
#
# m= int(sys.stdin.readline())
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     a_parent =[a]
#     b_parent =[b]
#
#     while p_list[a]:
#         a_parent.append(p_list[a])
#         a=p_list[a]
#
#     while p_list[b]:
#         b_parent.append(p_list[b])
#         b=p_list[b]
#
#     a_level = len(a_parent)-1
#     b_level = len(b_parent)-1
#     while a_parent[a_level] == b_parent[b_level]:
#         a_level -=1
#         b_level -=1
#     print(a_parent[a_level+1])

from math import *
import sys
sys.setrecursionlimit(5000000)
ip = sys.stdin.readline
n = int(ip())
pii = []
max_level = floor(log2(n))

#dp(ac)배열 만드는 과정
def getTree(nd, parent):
    # 현재노드의 깊이는 부모노드의 깊이 + 1
    depth[nd] = depth[parent] + 1

    # nd의 1번째 조상은 부모노드,2^0번째 조상
    ac[nd][0] = parent

    # MAX에 log를 씌워 내림해준다,
    for i in range(1,max_level+1):
        #tmp : nd의 2^(i-1)번째 조상

		# 즉, ac[nd][i] = ac[tmp][i-1]은
        # "현재 노드의 i번째의 조상은 (tmp의 2^(i-1)번째 조상)의 2^(i-1)번째 조상과 같다는 의미"
		# 예를들어 i=3일때 nd의 8번째 조상은 tmp(nd의 4번째 조상)의 4번째 조상과
		# 같다. i=4일때 nd의 16번째 조상은 nd의 8번째 조상(tmp)의 8번째와 같다.
        tmp = ac[nd][i-1]
        ac[nd][i] = ac[tmp][i-1] #현재노드 의 i번째의 조상은 tmp의 2^(i-1)번째 조상의 2^(i-1)번째 조상과 같다는 의미



    #dfs 알고리즘
    for i in graph[nd]:
        if i != parent: #재귀가 계속돌지 않도록 현재 자신의 부모노드가 아니면 재귀를 돈다.
            getTree(i,nd)

#양방향 그래프 형성
graph =[[] for i in range(n+1)]
depth = [0 for i in range(n+1)]
ac = [[0 for i in range(20)] for i in range(n+1)]

for i in range(n-1):
	a,b = map(int,ip().split())
	graph[a].append(b)
	graph[b].append(a)
#make_tree에 1,0이 들어가기때문에 0은 -1로 지정
depth[0] = -1

#루트노드인 1번노드부터 트리형성
getTree(1,0)

for i in range(int(input())):
     a,b = map(int,input().split())
     #깊이를 같게해주는 코드
     if depth[a] != depth[b]: #깊이가 같지않으면
         #depth[b] >= depth[a]가 되도록한다.
         if depth[a] > depth[b]:
             a,b = b,a
         # ac에 각각의 2^i의 조상이있기때문에 서로의 조상을 타고타고 들어가서 홀수도 가능한것이다.

         for i in range(max_level,-1,-1):
             #b의 2^i번째 조상이 a의 depth보다 크거나 같으면 계속 조상을 타고간다.
             if depth[a] <= depth[ac[b][i]]:
                 b = ac[b][i]

     lca = a
     #  a와 b가 다르다면 현재 깊이가 같으니
     # 깊이를 계속 올려 서로 다른 노드의 조상이 같아질 때까지 반복한다.
     # 즉, 서로 다른 노드(2,3)의 조상이 1로 같다면 lca = ac[2][0]에 의해 2의 조상이 1임을 알 수 있고
     # 마찬가지로 ac[3][0] 또한 3의 조상이 1임을 알게되며 알고리즘이 끝이난다.
     if a != b:
         for i in range(max_level,-1,-1):
             if ac[a][i] != ac[b][i]:
                 a = ac[a][i]
                 b = ac[b][i]
             lca = ac[a][i]
     print(lca)

