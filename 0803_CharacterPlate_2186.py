# from collections import deque
# N, M, K = map(int, input().split())
# plate = [' '.join(input()).split() for i in range(N)]
# target=input()
#
# answer =0
# dx=[]
# dy=[]
# for i in range(1,K+1):
#     dx.extend([-i,i])
#     dy.extend([-i,i])
# dx = dx + [0]*K*2
# dy = 2*K*[0] + dy
# q = deque()
# for i in range(N):
#     for j in range(M):
#         if plate[i][j] == target[0]:
#             q.append([i ,j, 0])
#             while q:
#                 row, col, n_iter = q.popleft()
#                 if n_iter == len(target)-1:
#                     answer +=1
#
#                 elif n_iter < len(target)-1:
#                     for k in range(4*K):
#                         nx = row + dx[k]
#                         ny = col + dy[k]
#                         if 0<=nx<N and 0<=ny<M and plate[nx][ny] == target[n_iter+1]:
#                             q.append([nx, ny, n_iter+1])
# print(answer)


from collections import deque
N, M, K = map(int, input().split())
plate = [' '.join(input()).split() for i in range(N)]
target=input()
answer =0
dx=[]
dy=[]
for i in range(1,K+1):
    dx.extend([-i,i])
    dy.extend([-i,i])
dx = dx + [0]*K*2
dy = 2*K*[0] + dy

q = deque()
for i in range(N):
    for j in range(M):
        if plate[i][j] == target[0]:
            dp = [[0 for _ in range(M)] for _ in range(N)]
            q.append([i ,j])
            dp[i][j] =0
            while q:
                row, col = q.popleft()
                if dp[row][col] == len(target):
                    answer +=1

                elif dp[row][col] < len(target):
                    for k in range(4*K):
                        nx = row + dx[k]
                        ny = col + dy[k]
                        if N <= nx or M <= ny or nx < 0 or ny <0:
                            continue
                        elif plate[nx][ny] == target[dp[row][col]+1]:
                            q.append([nx, ny])
                            dp[nx][ny] = dp[row][col] +1


print(answer)


