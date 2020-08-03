#
# F, S, G, U, D = map(int, input().split())
#
# visited =[True] +[False for i in range(F)]
# visited[S] =True
# move=[U,-D]
# q=[[0,S]]
# answer ='use the stairs'
# while q:
#     n_iter, fl = q.pop(0)
#     if fl == G:
#         answer = n_iter
#         break
#     for i in range(2):
#         move_fl =  fl + move[i]
#         if 1<= move_fl <=F and visited[move_fl] == False:
#             visited[move_fl] = True
#             q.append([n_iter+1,move_fl])
#
# print(answer)


#ver2
from collections import deque
F, S, G, U, D = map(int, input().split())

visited =[True] +[False for i in range(F)]
visited[S] =True
move=[U,-D]
q=deque()

answer ='use the stairs'

if S <G and U !=0:
    b = (G-S) // U
    S += b* U

elif S >= G and D !=0:
    b = (S - G) // D
    S -= b* D

q.append([b,S])

while q:
    n_iter, fl = q.popleft()
    if fl == G:
        answer = n_iter
        break
    for i in range(2):
        move_fl =  fl + move[i]
        if 1<= move_fl <=F and visited[move_fl] == False:
            visited[move_fl] = True
            q.append([n_iter+1,move_fl])

print(answer)





