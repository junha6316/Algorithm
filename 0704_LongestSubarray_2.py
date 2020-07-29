def solution(arr):
    N=len(arr)
    dp=[arr[0]]+[0 for _ in range(0,N-1)]

    for i in range(1,N):
        #if dp[i] == 0: dp[i] = arr[i]
        for j in range(i):
            if arr[i]>arr[j]:
                if dp[j]+arr[i]>dp[i]:
                    dp[i] = dp[j] + arr[i]

    return dp

def solution(arr):
    N = len(arr)
    dp = [arr[0]] + [0 for _ in range(0, N - 1)]
    for i in range(1,N):
        dp[i] = arr[i] +max(sum(dp[:i]))

    return dp

n = int(input())
a = list(map(int, input().split()))
c = [0] * 1001
for i in range(n): c[a[i]] = max(c[:a[i]]) + a[i]
print(max(c))


arr=[100,1 ,2 ,50 ,60 ,3, 5 ,6, 7, 8]

print(solution(arr))

'''
BOJ 제출용

N= int(input())
arr = list(map(int, input().split()))
dp =[arr[0]] + [0 for _ in range(0,N)]
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j] + arr[i] > dp[i]:
                dp[i] = dp[j] + arr[i]
                
print(max(dp))

'''
