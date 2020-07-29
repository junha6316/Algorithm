
def DFS(t):
    visited=[True]+[False for i in range(N)]
    dict = {i: [] for i in range(1, N + 1)}

    def rDFS(t,i):
        if visited[i] ==False:
            for idx, num in enumerate(t):
                if num[0] == i:
                    dict[i].append(num[1])
                    visited[idx] =True
                elif num[1] ==i:
                    dict[i].append(num[0])
                    visited[idx] = True

        print(dict) #돌때 인덱스가 없어져서 못
        print(t)

        for j in dict[i]:
            rDFS(t, j)

    for i in range(1, N+1):
        if visited[i] == False:
            rDFS(t,i)

    return dict


def solution(arr,N):
    visited =[False for i in range(N)]
    dict={i+1:[] for i in range(0,N)}
    result=[0 for _ in range(N+1)]
    def rDFS(arr, n):
        for i in range(N-1):
            if visited[i] == False:
                if arr[i][0] ==n:
                    visited[i] = True
                    result[arr[i][1]] =n
                    rDFS(arr, arr[i][1])

                elif arr[i][1] == n:
                    visited[i] = True
                    result[arr[i][0]] = n
                    rDFS(arr, arr[i][0])
    rDFS(arr,1)
    return result

# def solution(arr):
#     dic={1:[]}
#     visited=[False for _ in range(N-1)]
#     while(False in visited):
#         for idx, num in enumerate(arr):
#             if visited == False:
#                 num[1]
#                 visited[idx] = True
#
#     return dic


def solution(arr,N):
    visited =[False for i in range(N)]
    v=[False for i in range(N-1)]
    result =[0 for _ in range(N+1)]
    def rDFS(arr,n):
        print(visited)
        if visited[n-1] == False:
            visited[n-1] = True
            for idx,num in enumerate(arr):
                if  v[idx]==False:
                    if num[1] == n:
                        v[idx]=True
                        result[num[0]] =n
                        rDFS(arr,num[0])

                    elif num[0] == n:
                        v[idx] = True
                        result[num[1]] = n
                        rDFS(arr, num[1])

    rDFS(arr,1)
    return result


N= int(input())
arr = [list(map(int, input().split())) for i in range(N-1)]
answer= solution(arr,N)
for i in range(2,N+1):
    print(answer[i])




















