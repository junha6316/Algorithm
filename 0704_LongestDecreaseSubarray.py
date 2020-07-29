def solution(arr):
    N=len(arr)
    dp=[1] + [0 for _ in range(1,N)]
    for i in range(1,N):
        if dp[i] == 0: dp[i] =1
        for j in range(i):
            if arr[i] <arr[j]:
                if dp[j]+1 > dp[i]:
                    dp[i] =dp[j]+1
    return max(dp)

arr=[10, 30, 10, 20, 20, 10]

print(solution(arr))

''' BOJ 제출용'''

N= int(input())
dp=[1] +[0 for _ in range(1,N)]
for i in range(1, N):
    if dp[i] == 0: dp[i] = 1
    for j in range(i):
        if arr[i] < arr[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
print(max(dp))