from string import ascii_lowercase
def solution(num):
    N=len(num)
    dp=[1,1]+[0 for i in range(2,N+1)]
    if num[0] =='0':
        return 0
    for i in range(2,N+1):
        if int(num[i-2]+num[i-1]) <= 26 and int(num[i-2]+num[i-1]) >=10:
            dp[i] +=dp[i - 2]
        if int(num[i-1])>=1 and int(num[i-1]) :
            dp[i] += dp[i - 1]

    return dp[-1] % 1000000

num =input()
print(solution(num))



