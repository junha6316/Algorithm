from collections import deque
N=int(input())
mat=[[0 for i in range(N)] for i in range(4)]

for i in range(N):
    num = list(map(int, input().split()))
    for j in range(4):
        mat[j][i] = num[j]

A = mat[0]
B = mat[1]
C = mat[2]
D = mat[3]
answer=0
SUM=0
for a in A:
    SUM += a
    for b in B:
        SUM += b
        for c in C:
            SUM += c
            for d in D:
                SUM += d
                if SUM ==0:
                    answer +=1
                else:
                    SUM -=d

print(answer)
# answer=0
# def dfs(a,b,c,d):
#     global answer
#     if a==N or b==N or c==N or d==N:
#         return
#     if A[a] + B[b] +C[c] +D[d] ==0:
#         answer +=1
#
#
#     print(answer)
#
#     dfs(a + 1, b, c, d)
#     dfs(a, b + 1, c, d)
#     dfs(a, b, c + 1, d)
#     dfs(a, b, c, d + 1)
#
#     return
#
# dfs(0,0,0,0)
print(answer)


# visited=[[[[False for i in range(N)]for i in range(N)]for i in range(N)] for i in range(N)]

#
# point =(0, 0, 0, 0)
# q = deque()
# q.append(point)
# answer =0
#
# da =[1,0,0,0]
# db =[0,1,0,0]
# dc =[0,0,1,0]
# dd =[0,0,0,1]
# dic={}
# idx =0
# while q:
#     a,b,c,d=q.popleft()
#     if A[a] + B[b] +C[c] +D[d] ==0:
#         answer +=1
#
#     for i in range(4):
#         na,nb,nc,nd = a+da[i],b+db[i],c+dc[i],d+dd[i]
#         if na<N and nb<N and nc<N and nd<N:
#             if not visited[na][nb][nc][nd]:
#                 visited[na][nb][nc][nd]  = True
#                 q.append((na,nb,nc,nd))

print(answer)


