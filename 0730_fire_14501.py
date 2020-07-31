N=int(input())

consult = [[0,0]]
for i in range(1,N+1):
    dur, pay = map(int, input().split())
    consult.append([dur, pay])
dp = [0 for i in range(N+1)]

for i in range(1, N+1):
    if (consult[i][0] + i >N+1):
        continue
    max_price =0
    for j in range(1, i):
        if j + consult[j][0] <=i:
            max_price = max(dp[j], max_price)

    dp[i] = max_price + consult[i][1]

print(max(dp))