'''
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.                             a1 != a2
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.                          aN != aN-1
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.     a[i] != a[i-1] and ai != a[i+1]

입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
________________________________________________________________________________________________________________________
예시
26 40 83
49 60 57
13 89 99     12개
________________________________________________________________________________________________________________________
[86, 80] [89, 97] [132, 143]
[80, 89, 132]
________________________________________________________________________________________________________________________

i번째 집을 각각의 색으로 칠할 때, 1~i번째 집을 모두 칠하는 최소 비용으로 부분문제 정의
memo[i][0] = memo[i-1] + min(


#a[0] != a[2]
#a[N] != a[N-1]
#a[i] != a[i-1] and a[i] != a[i+1]

 [0,26] [1,40] [2,83]
 [2,83] 

memo[0][0][0] 

memo=[[0,0,0],
      [0,0,0],
      [0,0,0]]
밑에서 부터 올라간다.
'''


N = int(input())
p_rgb = []
for i in range(0, N):
    t =list(map(int, input().split()))
    p_rgb.append(t)

dp = [[0,0,0],  #dp[0]
      [0,0,0]]  #dp[1]

dp[0] = p_rgb[N-1]

for i in range(0, N-1): #0부터 N-2까지 N-1개
    i = (N-1)-i # N-1부터 1까지 N-1개
    for j in range(0, 3):
        if j == 0:
            dp[1][0] = p_rgb[i-1][0] + min(dp[0][1], dp[0][2]) #N-2부터 0
        elif j == 1:
            dp[1][1] = p_rgb[i-1][1] + min(dp[0][0], dp[0][2])
        else:
            dp[1][2] = p_rgb[i-1][2] + min(dp[0][0], dp[0][1])
    dp[0]=dp[1]
    dp[1]=[0,0,0]

print(min(dp[0]))

'''
 for j in range(0,3):
            if memo[0][j][0]==0:
                memo[1][j][1] = memo[0][0][1] + min(p_rgb[i][1], p_rgb[i][2])
                memo[1][j][0] = p_rgb[i].index(min(p_rgb[i][1], p_rgb[i][2]))

            elif memo[0][j][0]==1:
                memo[1][j][1] = memo[0][1][1] + min(p_rgb[i][0], p_rgb[i][2])
                memo[1][j][0] = p_rgb[i].index(min(p_rgb[i][0], p_rgb[i][2]))
            else:
                memo[1][j][1] = memo[0][2][1] + min(p_rgb[i][0], p_rgb[i][1])
                memo[1][j][0] = p_rgb[i].index(min(p_rgb[i][0], p_rgb[i][1]))
'''





