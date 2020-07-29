N,M = map(int, input().split())
rectangle =  [list(map(int, ' '.join(input()).split())) for i in range(N)]
Sum=[[0 for i in range(M)] for i in range(N)]
Sum[0][0] = rectangle[0][0]
for i in range(0,N):
    for j in range(0,M):
        if i==0 and j==0:
            pass
        elif i == 0:
            Sum[i][j] =Sum[i][j - 1]+ rectangle[i][j]
        elif j==0:
            Sum[i][j] = Sum[i - 1][j] + rectangle[i][j]
        else:
            Sum[i][j] = Sum[i-1][j] + Sum[i][j-1] - Sum[i-1][j-1]+ rectangle[i][j]


def SUM(a,b,c,d):
    if a==0 and b==0:
        return Sum[c][d]
    elif a==0:
        return Sum[c][d] -Sum[c][b-1]
    elif b==0:
        return Sum[c][d]- Sum[a - 1][d]
    else:
        return Sum[c][d] - Sum[c][b - 1] - Sum[a - 1][d] + Sum[a - 1][b - 1]

ans=0
for i in range(0,M-2):
    for j in range(i+1,M-1):
        r1 = SUM(0,0,N-1,i)
        r2 = SUM(0,i+1,N-1,j)
        r3 = SUM(0,j+1,N-1,M-1)
        if ans < r1*r2*r3:
            ans= r1*r2*r3

for i in range(0,N-2):
    for j in range(i+1,N-1):
        r1 = SUM(0,0,i,M-1)
        r2 = SUM(i+1,0,j,M-1)
        r3 = SUM(j+1,0,N-1,M-1)
        if ans < r1*r2*r3:
            ans= r1*r2*r3


for i in range(0,N-1):
    for j in range(0,M-1):
        r1 = SUM(0, 0, i, j)
        r2 = SUM(0, j+1, i, M - 1)
        r3 = SUM(i+1, 0, N - 1, M - 1)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(0,N-1):
    for j in range(0,M-1):
        r1 = SUM(0, 0, N-1, j)
        r2 = SUM(0, j+1, i, M - 1)
        r3 = SUM(i+1, j+1, N - 1, M - 1)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

