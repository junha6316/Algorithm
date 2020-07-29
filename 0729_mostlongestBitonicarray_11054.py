N=int(input())
num_li =[0]+ list(map(int, input().split()))

def increaseArray(num_li):
    global N
    dp = [[0, 0] for i in range(N+1)]
    dp[1] = [num_li[1], 1]
    for i in range(1,N+1):
        dp[i][0] = num_li[i]
        for j in range(i-1,0,-1):
            if dp[j][0] < num_li[i]:
                dp[i][1]=max(dp[i][1] ,dp[j][1]+1)

    return dp

def decreaseArray(num_li):
    global N
    dp = [[0, 0] for i in range(N+1)]
    dp[-1] = [num_li[-1],0]
    for i in range(N-1,0,-1):
        dp[i][0] = num_li[i]
        for j in range(i+1,N+1):
            if dp[j][0] < num_li[i]:
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)
    return dp
if N<3:
    print(0)
else:
    MAX=0
    for inc, dec in zip(increaseArray(num_li), decreaseArray(num_li)):
        if  MAX < inc[1]+dec[1]:
            print(MAX)





