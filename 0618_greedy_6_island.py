'''
문제 설명
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항

섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.

임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는
다리가 연결되는 두 섬의 번호가 들어있고, costs[i][2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
입출력 예

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	0 1 2 3
입출력 예 설명
0 1 2 0
1 0 2 1
2 2 0 8
0 1 8 0
costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.
[[999, 1, 2, 999],
[999, 999, 5, 1],
[999, 999, 999, 8],
[999, 999, 999, 999]]
'''

def solution(n, costs):
    mat=[[999 for i in range(n)] for i in range(n)]
    for cost in costs:
        mat[cost[0]][cost[1]] =cost[2]

    init =(0,0)
    while(True):
       mini = min(mat[init[0]][init[1]+1],mat[init[0]+1][init[1]+1])
       mat[0][0] += mini
       init[0] = mat.index(mini)[0]
       init[1] = mat.index(mini)[1]

       if init[1] == n-1:
           break

    return mat



import heapq as hq

def solution(n, costs):
    answer = 0
    from_to = list(list() for _ in range(n)) #빈 리스트[ []*n]
    visited = [False] * n #방문했는지 하지 않았는지를 확인한다.
    priority = [] #우선순위

    for a, b, cost in costs:
        from_to[a].append((b, cost)) #현재 위치에서 갈 수 있는 곳  // 행 : 현재 위치 //열 : (갈 수 있는 곳, 비용)
        from_to[b].append((a, cost)) #양방향으로 갈 수 있음

    hq.heappush(priority, (0, 0)) #힙에 (0,0)을 넣는다. #cost 기준으로 오름차순으로 정렬된다.(78 확인)

    while False in visited: #방문리스트에 False가 있으면
        cost, start = hq.heappop(priority)
        if visited[start]: continue #방문 했다면 다음으로 넘긴다.

        visited[start] = True       #방문하지 않았다면 방문리스트에서 해당 인덱스를 True로 바꾼다.
        answer += cost              #정답에 cost를 더한다.
        for end, cost in from_to[start]:
            if visited[end] ==True : continue #방문한 곳이라면 다시 뽑는다.
            else:
                hq.heappush(priority, (cost, end)) #방문하지 않은 곳이라면 다시 넣는다.

    return answer

'''
가지 않은 곳 중에서 cost가 가장 작은 값들을 더한다 => greedy
'''

def solution(n, costs):
    answer =0
    fromTo = [[] for _ in range(n)]
    check = [False for _ in range(n)]

    for start,end, cost in costs:
        fromTo[start].append((end, cost))
        fromTo[end].append((start,cost))

    priority=[]
    # hq.heapify(priority) 어차피 비어있기 때문에 하지 않아도 된다.
    hq.heappush(priority, (0,0)) #(cost, to)

    while (False in check):
        cost, start = hq.heappop(priority)
        if check[start] == True:
            continue

        check[start] =True
        answer += cost
        for end, cost in fromTo[start]:
            if check[end] == True:
                continue
            else:
                hq.heappush(priority,(cost,end))

    return answer

n =4
costs =[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))