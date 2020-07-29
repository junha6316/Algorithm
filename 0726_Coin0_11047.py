N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
i =0
cnt =0
while(K != 0):
    for idx, num in enumerate(coins):
        if K < num:
            cnt += K // coins[idx - 1]
            K = K % coins[idx - 1]
            break

    if idx == N-1:
        cnt += K // coins[N-1]
        K = K % coins[N - 1]

print(cnt)

