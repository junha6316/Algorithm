def solution(N):
    memo=[1,3]
    smemo =[]
    if N==1:
        return 1
    elif N==2:
        return 3

    for i in range(2,N):
        if (i+1) % 2 ==1:
            memo.append(2*memo[i-1]-1)
        else:
            memo.append(2 * memo[i - 1] + 1)

    return memo[-1]

print(solution(12))