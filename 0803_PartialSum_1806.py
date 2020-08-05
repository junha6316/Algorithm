N, M = map(int, input().split())

num= list(map(int, input().split()))
start =0
end=0
SUM =0
MIN = 99990

while(True):
    if SUM >= M:
        ans =min(ans,k)
        SUM -= num[start]

    else:
        if end ==N:
            break
        SUM += num[end]
        end += 1


if MIN == 99990:
    print(0)
else:
    print(MIN)


n, m = map(int, input().split())
a = list(map(int, input().split()))

def solve():
    start = end = k = s = 0
    answer =0
    while True:
        if s >= m:
            if s == m:
                answer +=1
            s -= a[start]
            start += 1

        else:
            if end == n:
                break
            s += a[end]
            end += 1
    print(answer)

solve()




