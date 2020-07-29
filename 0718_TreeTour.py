
# tree = {chr(65+i):[] for i in range(N)}
# for i in range(N):
#     p, *c = input().split()
#     tree[p].extend(c)
# def pretour(tree):
#     visited =[False for i in range(N)]
#     tour =''
#     def rDFS(tree, root):
#         idx = ord(root) -65
#         if visited[idx] == False:
#             visited[idx]= True
#             nonlocal tour
#             tour += root
#             for i in tree[root]:
#                 if i == '.': pass
#                 elif visited[ord(i) - 65] == False:
#                     rDFS(tree, i)
#
#     rDFS(tree, 'A')
#     return tour
#
# print(pretour(tree))
# N=int(input())
# parent =[0 for i in range(N)]
# child=[[] for i in range(N)]
# for i in range(N):
#     p , *c = input().split()
#     idx = ord(p)-65
#     child[idx] =c
#     for j in c:
#         if j =='.':pass
#         else:parent[ord(j)-65] = idx
#
# print(parent)
#
# def pretour(child):
#     visited =[False for i in range(N)]
#     tour =''
#     def rDFS(root):
#         idx = ord(root) - 65
#         if visited[idx] == False:
#             visited[idx] = True
#             nonlocal tour
#             tour += root
#
#             for i in child[idx]:
#                 if i == '.': pass
#                 elif visited[ord(i) - 65] == False:
#                     rDFS(i)
#     rDFS('A')
#
#     return tour
#
# print(pretour(child))
#
# def findep(root,child):
#     while(True):
#         idx = ord(root) - 65
#         st = child[idx][0]
#         if st == '.':
#             return root
#         else:
#             root = st
#
# def midtour(child,parent):
#     visited = [False for i in range(N)]
#     tour = ''
#     def rDFS(root):
#         idx = ord(root)-65
#         if child[idx][0] !='.' and visited[idx]==False:
#             rDFS(child[idx][0])
#
#         elif visited[ord(child[idx][0])-65] ==True:
#             nonlocal tour
#             tour += root
#
#         else:
#             visited[idx] = True
#             tour += root
#
#             if child[parent[idx]][1] != '.':
#                 rDFS(child[parent[idx]][1])
#             else:
#                 rDFS(chr(parent[idx]+65))
#
#
#
#
#
#     rDFS('A')
#
#     return tour
#
#
#
# print(midtour(child,parent))

import sys
sys.setrecursionlimit(10**6)
def preorder(node):
    if node == '.':
        return
    print(node, end = "")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end = "")
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end = "")

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')


