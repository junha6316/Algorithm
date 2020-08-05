N, M = map(int, input().split())
num_li = list(map(int, input().split()))

answer =0
SUM =0
start, end = 0, 0

while(start <= N-1):
    if SUM >= M or end ==N:
        if SUM == M:
            answer +=1

        SUM -= num_li[start]
        start += 1

    elif SUM < M and end <= N-1:
        SUM += num_li[end]
        end += 1
print(answer)





