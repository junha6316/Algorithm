import sys
def solution(arr):
    stack =0
    answer =0
    for idx, item in enumerate(arr):
        if item =='(':
            if arr[idx+1] =='(':
                stack +=1
                answer +=1
            else:
                answer += stack
        else:
            if arr[idx-1:idx+1] =='()':
                pass
            else:
                stack -=1

    return answer
arr= sys.stdin.readline()[:-1]
print(solution(arr))
