def solution(N,K):
    dp = [[0 for _ in range(N)] for _ in range(K)]
    dp[0]=[1 for _ in range(N)]
    for i in range(1,K):
        dp[i][0] = i+1
        for j in range(1,N):
            dp[i][j] = dp[i-1][j] +dp[i][j-1]

    return dp[-1][-1] % 1000000000

N,K=tuple(map(int, input().split()))
print(solution(N,K))
