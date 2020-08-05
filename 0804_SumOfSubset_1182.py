N, S = map(int, input().split())
num_li = list(map(int, input().split()))
answer=0

A, B= num_li[:N//2], num_li[N//2:]
tableA, tableB ={}, {}
def dfs(n,sum_, i, o):
    #n은 카운터
    if n == len(i):
        o[sum_] = o.get(sum_,0) +1
        return

    dfs(n+1, sum_, i, o)
    dfs(n+1, sum_+i[n], i,o)

dfs(0,0, A, tableA)
dfs(0,0, B, tableB)

tableA[0] -=1
tableB[0] -=1

ans = tableA.get(S,0)+ tableB.get(S,0)

for i in tableA:
    if S-i in tableB:
        ans += tableB[S-i]*tableA[i]
print(ans)

#
# def dfs(idx,total):
#
#     if idx >= N:
#         return
#     total += num_li[idx]
#     if total ==S:
#         global answer
#         answer +=1
#
#     dfs(idx+1, total-num_li[idx])
#     dfs(idx+1, total)
#
# dfs(0,0)
# print(answer)


