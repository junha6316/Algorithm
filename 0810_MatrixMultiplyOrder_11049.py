N= int(input())
matrix= [(0,0)]+[tuple(map(int, input().split())) for i in range(N)]

if N== 1:
    print(0)
else:
    dp = [0 for i in range(N + 1)]
    dp[2] = matrix[1][0] * matrix[1][1] *matrix[2][1]


    for i in range(3, N+1):
        print(dp[i-1],matrix[1][0],matrix[i-1][1],matrix[i][1])
        print(dp[i-2],matrix[i-1][0],matrix[i-1][1],matrix[i][1] , matrix[1][0],matrix[i-1][0],matrix[i][1])
        dp[i] = min(dp[i-1] + matrix[1][0]*matrix[i-1][1]*matrix[i][1],
                    dp[i-2] + matrix[i-1][0]*matrix[i-1][1]*matrix[i][1] + matrix[1][0]*matrix[i-1][0]*matrix[i][1])

    print(dp)


'''
5
5 3
3 2
2 6
6 4
4 5
'''


