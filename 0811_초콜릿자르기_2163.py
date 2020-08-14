N, M = map(int, input().split())

ch = [[0 for i in range(M+1)] for j in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if i== 1:
            ch[i][j] = j -1
        elif j ==1:
            ch[i][j] = i-1
        else:
            ch[i][j] = ch[i-1][j] + j

print(ch[N][M])


