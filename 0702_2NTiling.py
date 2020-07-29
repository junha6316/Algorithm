def solution(N):

    #memos=[[1,1]] + [[0,0] for i in range(N-1)] # [tno doble, tno one]
    if N==1:
        return 1
    memo=[1,2]
    for i in range(2,N):
        memo.append(memo[i-2]+memo[i-1])

    return memo[-1]

print(solution(10))


