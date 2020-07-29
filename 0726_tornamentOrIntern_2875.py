N, M, K = map(int, input().split())

MAXI =0
for i in range(0,K+1):
    (i,K-i)
    if N > i and M > K-i:
        MAXI = max(MAXI, min((N - i) // 2, (M - K+i) // 1))

print(MAXI)

