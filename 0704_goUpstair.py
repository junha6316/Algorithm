def solution(arr):
    N= len(arr)
    if N==1:
        return arr[0]
    else:
        DP = [0, arr[0], arr[0] + arr[1]] + [0 for _ in range(3, N+1)]
        arr=[0] + arr
        for i in range(3,N+1):
            if i ==N:
                DP[i] = arr[i] + DP[i - 2]
                DP[i] = max(DP[i], arr[i - 1] + arr[i] + DP[i - 3])

            else:
                DP[i] = max(arr[i] + DP[i-2], DP[i-3] + arr[i-1] + arr[i])
            print(DP,arr[i])
    return DP[-1]

arr=[10,20,20,15,25,10]#,20]
print(solution(arr))
#
# import sys
# N = int(input())
# arr = [int(sys.stdin.readline()) for i in range(N)]
# if N ==1:
#     print(arr[0])
# else:
#     DP = [0, arr[0], arr[0] + arr[1]] + [0 for _ in range(3, N)]
#     arr = [0] + arr
#     for i in range(3,N):
#             DP[i] = max(arr[i] + DP[i - 2], arr[i - 1] + arr[i] + DP[i - 3])
#     print(DP)



