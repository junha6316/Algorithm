# import sys
# def LCA(a,b):
#     if an[a][0]>an[b][0]:
#         a = an[a][1]
#         LCA(a,b)
#
#     elif an[a][0]<an[b][0]:
#         b = an[b][1]
#         LCA(a, b)
#
#     else:
#         if a==b:
#             print(a)
#         else:
#             while an[a][1] != an[b][1]:
#                 a= an[a][1]
#                 b= an[b][1]
#
#             print(an[a][1])
#
#
# N= int(sys.stdin.readline())
# dic ={i:[] for i in range(1, N+1)}
# visited =[True, True]+[False for i in range(1,N)]
# an ={i:0 for i in range(1,N+1)}
# an[1] =(0,1)
# for i in range(1,N):
#     n1, n2 = map(int, sys.stdin.readline().split())
#     dic[n1].append(n2)
#     dic[n2].append(n1)
# q=[]
# q.append((1,1)) #(depth, N_node)
#
# while(q):
#     depth, node=q.pop(0)
#     for ch in dic[node]:
#         if visited[ch] == False:
#             visited[ch] = True
#             q.append((depth+1, ch))
#             an[ch] = (depth, node)
#
#
# # m = int(sys.stdin.readline())
# # for i in range(m):
# #     a, b = map(int, sys.stdin.readline().split())
# #     LCA(a,b)
#
#
# LCA(1,1)
#
import sys


N= int(sys.stdin.readline())
p_list = [0 for _ in range(N+1)]
for _ in range(N-1):
    p, c = map(int, sys.stdin.readline().split())
    p_list[c] =p

m= int(sys.stdin.readline())
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a_parent =[a]
    b_parent =[b]

    while p_list[a]:
        a_parent.append(p_list[a])
        a=p_list[a]

    while p_list[b]:
        b_parent.append(p_list[b])
        b=p_list[b]

    a_level = len(a_parent)-1
    b_level = len(b_parent)-1
    while a_parent[a_level] == b_parent[b_level]:
        a_level -=1
        b_level -=1
    print(a_parent[a_level+1])



