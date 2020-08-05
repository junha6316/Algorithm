

distance= 25
rocks = [2, 14, 11, 21, 17]
n=2

print(solution(rocks, n, distance))

def solution():

visited =[False for i in range(n)]
answer =[]
def deleteRock(i, cnt):
    global n
    if cnt == n:
        for i in range(n):
            if visited[i]:
                answer.append(rocks[i])
        return answer

    answer=[]

    for j in range()
        visited[i] = 1
        deleteRock(i+1, cnt+1)
        visited[i] =0

