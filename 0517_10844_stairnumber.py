'''
45656이란 수를 보자.
이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)
입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.력

자릿수가 N인 계단 수를 찾는 문제
시작시간 : 05/17 16:46
끝 시간 : 05/17 17:52

N= int(input())
10^n ~ 10^(n+1) -1

123 234 345 345 456 567 678 789 898
N=1 9
1  2  3  4  5  6  7  8  9
N=2 17
10 23 34 45 56 67 78 89     17*2
12 21 32 43 54 65 76 87 98
N=3
101 210 321
121 212 323
123 232 343
    234 345

a0 a1    aN-1

a0 : 1,2,3,4,5,6,7,8,9 9
a1 : a0-1, a0+1        2   if a0 ==9 a1:8
a2 : a1-1, a1+1
'''

N=3

'''
def find_stair(N):
    num_st =0
    num_st_li =[0, 1 for i in range(0,9)]
    if N==1:
        num_st = 9
        num_st_li.append(num_st)
        return num_st
    else:
        for i in range(0,N):
            num_st
    return 0
'''

import copy


import copy

def cov():
    N= int(input())
    if N==1:
        print(9)
        return
    else:
        N= N-1
        num_st_li =[0]+ [1 for i in range(0,9)]
        dp = [num_st_li, [0 for i in range(0,10)]]  #[[N 일때], [N+1일 때]]

        for j in range(0,N):
            for i in range(0,10):
                if i ==0:
                    dp[1][0] = dp[0][1]
                elif i==9:
                    dp[1][9] = dp[0][8]
                else:
                   dp[1][i] = dp[0][i-1] + dp[0][i+1]
            dp[0] = copy.deepcopy(dp[1])

        print(sum(dp[1]) % 1000000000)

    return

cov()
