


def solution(K, travel):

    walk = [[travel[i][0],travel[i][1]] for i in range(len(travel))]
    byci = [[travel[i][2],travel[i][3]] for i in range(len(travel))]
    gap=[0 for i in range(len(travel))]
    dp=[]
    answer =0
    t=0

    for time, money in walk:
        answer += money
        t += time

    t= t-K # 메꿔야하는 시간

    for i in range(len(travel)):
        gap[i] =[walk[i][0]-byci[i][0],walk[i][1]-byci[i][1]]

    gap= sorted(dp, key=lambda x:x[1])

    for idx, d in enumerate(gap):
        '''
        여기까지 내가한 부분
        #gap= sorted(gap, key=lambda x:x[])
        #dp[i][0] 바꿨을 때 추가되는 시간, dp[i][1] 빠지는 돈
        #빠지는 돈이 제일 작으면서 시간이 커야한다.
       '''
    return dp


#------
def solution(K, travel):
    n=len(travel)

    memo=[[0 for j in range(K+1)] for x in range(n+1)] #(n+1) * (K+1)행렬을 만듦

    for i in range(1,n+1):
        t_walk, v_walk, t_bike, v_bike = travel[i-1] #마지막 값을 저장해둔다.

        for j in range(K+1): #K번 반복하는데
           #walk
            walk = (memo[i-1][j-t_walk] + v_walk) if j >= t_walk and memo[i-1][j-t_walk] != -1 else -1
            bike = (memo[i-1][j-t_bike] + v_bike) if j >= t_bike and memo[i-1][j-t_bike] != -1 else -1

            memo[i][j]= max(walk,bike)

    for i in range(len(memo)):
        for j in range(len(memo[i])):
            memo[i][j] =(memo[i][j], j)
    return memo[2]

K= 1650
travel = [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]

# K=3000
# travel = [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]

print(solution(K, travel))