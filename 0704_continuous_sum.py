def solution(arr):
    N = len(arr)
    DP=[arr[0]]+[0 for _ in range(1,N)]
    Max=arr[0]


    for i in range(1,N):
        Max = max(Max+arr[i], arr[i])
        DP[i] = max(DP[i-1],Max,arr[i])

    return DP


arr=[2, 1, -4, 3, 4, -4, 6, 5, -5, 1]
arr=[10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
arr=[-1, -2, -3 ,-4, -5]
print(solution(arr))

N= int(input())
arr=list(map(int, input().split()))
DP=[arr[0]]+[0 for _ in range(1,N)]
SUM=[arr[0]]

for i in range(1, N):
    Max = max(Max + arr[i], arr[i])
    DP[i] = max(DP[i - 1], Max, arr[i])

print(max(DP))
