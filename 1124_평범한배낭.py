N, K = map(int, input().split())
values = [0 for _ in range(N+1)]
weights = [0 for _ in range(N+1)]

for i in range(1,N+1):
    weight, value = map(int, input().split())
    weights[i] =weight
    values[i] =value
    
    
dp =[[0 for _ in range(K+1)] for i in range(N+1)]
for i in range(1, N+1):
    weight = weights[i]
    value = values[i]
    for j in range(1, K+1):
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            if value + dp[i-1][j-weight] > dp[i-1][j]:
                dp[i][j]= value + dp[i-1][j-weight]
            else:
                dp[i][j] =dp[i-1][j]
       

print(dp[i][j])
