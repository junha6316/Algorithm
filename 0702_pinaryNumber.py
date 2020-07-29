#N자리 pinary number

"""
not start with 0 => N-1 자리
not exist "11"
"""

def solution(N):
    answer=[]
    i=0
    li=[]
    while(i<N-1):
        for idx ,num in enumerate(answer):
            if num[-1] =='1':
                li.append(answer[idx]+'0')

            elif num[-1] =='0':
                li.append(answer[idx]+'0')
                li.append(answer[idx]+'1')

        answer =li
        li=[]
        i+=1


    return len(answer)

def solution(N):

    i=1
    memo=[[0,1]]+[[0,0] for _ in range(N-1)]
    while(i<=N-1):

        memo[i][0] = memo[i-1][0] + memo[i-1][1]
        memo[i][1]= memo[i-1][0]
        i+=1

    return sum(memo[-1])



print(solution(3))





