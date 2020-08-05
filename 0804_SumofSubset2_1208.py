N, S = map(int, input().split())
num = list(map(int, input().split()))
answer=0
A, B = num[:N//2], num[N//2:]
tableA, tableB ={}, {}

def solution(n,sum_,i,o):
    if n ==len(i):
        o[sum_] =o.get(sum_,0) +1
        return
    solution(n+1, sum_+i[n],i,o)
    solution(n+1, sum_, i, o)

solution(0,0,A,tableA)
solution(0,0,B,tableB)
print(tableA)
print(tableB)

answer = tableA.get(S,0) + tableB.get(S,0)

tableA[0] -=1
tableB[0] -=1

for i in tableA:
    if S-i in tableB:
        answer += tableA[i]*tableB[S-i]

print(answer)


