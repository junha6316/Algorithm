
def solution(n, computers):
    answer = 0
    network ={i:[] for i in range(1,n+1)}
    visited =[True]+[False for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i !=j and computers[i][j] ==1:
                network[i+1].append(j+1)
                network[j+1].appned(i+1)

    def dfs():
        answer=0
        def rdfs(i):
            visited[i] =True
            for j in network[i]:
                if not visited[j]:
                    rdfs(j)

        for i in range(1,n):
            if not visited[i]:
                rdfs(i)
                answer +=1
    dfs()

    return answer

def solution(n, computers):
    answer=0
    visited =[0 for i in range(n)]
    def dfs(computers, visited, start):
        stack=[start]
        while(stack):
            j=stack.pop()
            if visited[j] ==0:
                visited[j]=1

            for i in range(0, n