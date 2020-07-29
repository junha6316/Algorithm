# import sys
# def solution(N,arr):
#     dp=[[0 for i in range(len(arr)+1)] for i in range(0,N+1)]
#
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             if j<= i:
#                 dp[i][j] = max(dp[i][j-1], arr[j-1]+dp[i-j][j])
#             else:
#                 dp[i][j] = dp[i][j-1]
#
#     return dp[-1][-1]
#
# N= int(sys.stdin.readline())
# arr=list(map(int, input().split()))
# print(solution(N,arr))
#
# import sys
# N = int(sys.stdin.readline())
# price = list(map(int, sys.stdin.readline().split()))
#
# max_list = [price[0]]
# for n in range(2,N+1):
#     max_p = max([i+j for i,j in zip(price[0:n-1][::-1], max_list)])
#     max_p = max(max_p, price[n-1])
#     max_list.append(max_p)
# print(max_list[-1])
#
#
#

import sys
from collections
N= int(sys.stdin.realline())

card = [0]+list(map(int, sys.stdin.readline().split()))

for i in range(2,N+1):
    for j in range(1,i//2+1):
        if card[i] < card[j] +card[i-j]:
            card[i] = card[j]+card[i-j]


print(card[N])































