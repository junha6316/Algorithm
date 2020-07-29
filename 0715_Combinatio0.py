# n, m = map(int, input().split())

def find0_1(n,m):
    answer =0
    for i in range(m, n + 1):
        if i % 5 == 0 and i >= 5:
            while (i % 5 == 0):
                i = i // 5
                answer += 1
    return answer

n, m = map(int, input().split())
def find5(n):
    i=5
    answer=0
    while(i<=n):
        answer += n//i
        i *= 5
    return int(answer)

def find2(n):
    i=2
    answer=0
    while(i<=n):
        answer += n//i
        i *= 2
    return int(answer)

def solution(n,m,i):
    if i == 2:
        return(find2(n)-find2(n-m)-find2(m))
    else:
        return(find5(n)-find5(n-m)-find5(m))

print(min(solution(n,m,2),solution(n,m,5)))