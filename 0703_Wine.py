def solution(W):
    n =len(W)
    dp =[0 for _ in range(0,n)]
    dp[0] = W[0]
    dp[1] = W[0]+W[1]
    if n ==1:


    for i in range(2,n):
        dp[i] = max(dp[i - 2] + W[i], dp[i - 3]+ W[i-1]+W[i])
        dp[i] = max(dp[i-1], dp[i])

    return max(dp)

W=[1]
print(solution(W))







