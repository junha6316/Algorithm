def solution(N):
    dp=[0 for i in range(N+1)]

    dp[0] = 1
    dp[1] = 0
    dp[2] = 3
    for i in range(3,N+1):
        dp[i]= 3*dp[i-2]
        for j in range(3,i+1):
            if j % 2 ==0:
                dp[i] += 2*dp[i-j]
    return dp[-1]

print(solution(8))






N=int(input())
def solution(n):
    dp=[0, 0, 3] + [0 for i in range(3,n+1)]
    for i in range(3,n+1):
        if i % 2 ==0:
            dp[i] = 3 * dp[i - 2] + 2

    return dp[n]

print(solution(N))






















