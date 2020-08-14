#인접한 노드사이의 비용을 표시한 2차원 배열을 만든다.

N= int(input())
dp =[[float('inf') for i in range(N+1)] for i in range(N+1)]
M = int(input())

for i in range(M):
    s, e, c = map(int, input().split())
    if dp[s][e] != float('inf'):
        dp[s][e] = min(c, dp[s][e])
    else:
        dp[s][e] = c

for i in range(1,N+1):
    for row in range(1,N+1):
        for col in range(1,N+1):
            if col !=i and row != col: #i번째 노드를 거쳐서 row에서 col로 가는 경우
                dp[row][col] = min(dp[row][col], dp[row][i] + dp[i][col])


for i in range(1,N+1):
    for j in range(1, N+1):
        if dp[i][j] == float('inf'):
            dp[i][j] =0


for i in range(1,N+1):
    print(' '.join(map(str, dp[i][1:])))
