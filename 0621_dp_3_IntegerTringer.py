def solution(triangle):
    answer = 0
    dp=[triangle[-1], triangle[-2]]

    for i in range(1,len(triangle)-1):
        for j in range(len(dp[1])):
            '''
            dp[0] 5개
            dp[1] 4개
            '''
            dp[1][j] =dp[1][j]+ max(dp[0][j],dp[0][j+1])
        dp[0] = dp[1]
        dp[1] = triangle[-i-2]



    return  dp[1][0] + max(dp[0])

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


print(solution(triangle))