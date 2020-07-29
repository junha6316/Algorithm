# # -*- coding: utf-8 -*-
# def solution(arrs):
#     n=len(arrs[0])
#     answer =0
#     chk= [[False for _ in range(n)] for arr in arrs]
#
#     arrs = [(arrs[i][j], i, j) for j in range(n) for i in range(len(arrs))]
#     arrs.sort(reverse=True)
#
#     while(len(arrs) != 0):
#         max, i, j = arrs.pop(0)
#         answer += max
#         chk[i+1][j] =True if chk[i+1][j]
#         chk[i-1][j] = True if chk[i-1][j]
#         chk[i][j-1] = True if chk[i][j-1]
#         chk[i][j+1] = True if chk[i][j+1]
#
#         arrs.sort(reverse=True)
#         print(answer)
#
#     return answer

'''
D[N][M] : N번째 열에서 스티커를 M했을 때, 2xN 개의 스티커에서 얻을 수 있는 최대 점수 0,1,2

M = 0 (위쪽 스티커를 뜯음), M = 1 (아래쪽 스티커를 뜯음), M = 2 (둘 다 뜯지 않음)
D[1][0] = P[1][0], D[1][1] = P[1][1], D[1][2] = 0

D[N][0] : N번째 열에서 위쪽 스티커를 뜯어서 얻은 최대 점수
D[N][1] : N번째 열에서 아래쪽 스티커를 뜯어서 얻은 최대 점수
D[N][2] : N번째 열에서 둘 다 뜯지 않고 얻은 최대 점수
'''

def solution(P):
    N=len(P[0])
    print(N)
    D = [[0,0,0] for _ in range(N)]
    D[0][0] = P[0][0]
    D[0][1] = P[1][0]
    D[0][2] = 0

    for i in range(1,N):
        D[i][0] = max(D[i-1][1], D[i-1][2]) + P[0][i]
        D[i][1] = max(D[i-1][0], D[i-1][2]) + P[1][i]
        D[i][2] = max(D[i-1][0], D[i-1][1], D[i-1][2])

    return max(D[-1])




arrs= [[50, 10, 100, 20, 40],
       [30, 50, 70, 10, 60]]

print(solution(arrs))