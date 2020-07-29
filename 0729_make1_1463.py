N= int(input())

if N <=3:
    if N==1: print(0)
    elif N==2: print(1)
    elif N==3:print(1)
else:
    dp = [0 for i in range(N + 1)]
    dp[1], dp[2], dp[3] =0, 1, 1
    for i in range(4,N+1):
        if i %6 ==0:
            dp[i]=min(dp[i - 1] + 1, dp[i // 3] + 1, dp[i//2]+1)
        elif i%3 ==0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 3] + 1)
        elif i %2==0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else: #3,2로 안나눠지는경우 홀수
            dp[i] = dp[i-1]+1

    print(dp[N])

'''
  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
0 0 1 1 2 3 2 3 3 2 3 

'''