# print(answer)



from itertools import permutations
n=int(input())
d=[list(map(int, input().split())) for i in range(n)]

city = [i for i in range(n)]
answer = 100000000
def totalCost(case):
    global d, n
    cost =0
    for i in range(n-1):
        if d[case[i]][case[i+1]] !=0:
            cost += d[case[i]][case[i+1]]
        else:
            return -1

    if d[case[-1]][case[0]] ==0:
        return -1
    else:
        cost += d[case[-1]][case[0]]

    return cost

for c in permutations(city):
    COST = totalCost(c)
    if COST != -1:
        answer = min(answer,COST)

print(answer)