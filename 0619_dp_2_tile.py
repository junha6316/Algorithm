def solution(n):
    dp=[0,1]
    for i in range(n):
        temp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = temp

    return 2*(dp[0] +dp[1])

n =5

print(solution(n))