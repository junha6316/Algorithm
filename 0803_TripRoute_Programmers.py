
def solution(tickets):
    start ='ICN'
    answer = []
    tickets = sorted(tickets, key=lambda x:x[1])

    while tickets:
        start_temp, end_temp = tickets.pop(0)
        if start == start_temp:
            answer.append(start_temp)
            start = end_temp
        else:
            tickets.append([start_temp, end_temp])
        if not tickets:
            answer.append(end_temp)

    return answer

def solution(tickets):
    n= len(tickets)
    answer = ['ICN']
    iternary = {}

    for start, end in tickets:
        if not iternary.get(start):
            iternary[start]=[end]
        else:
            iternary[start].append(end)
            iternary[start].sort()

        if not iternary.get(end):
            iternary[end] = []

    n_iter= 0
    start = 'ICN'
    answer = []

    def rdfs(start):
        if iternary[start] == []:
            answer.append(start)
            return

        answer.append(start)
        end = iternary[start].pop(0)
        rdfs(end)

    rdfs(start)
    print(iternary)
    return answer
tickets=[['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]

tickets=[['ICN', 'SFO'] ,['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]

#tickets=[['ICN', 'JFK'],['JFK','AMD'],['AMD','ICN']]

print(solution(tickets))

def solution(tickets):
    routes={}
    for start, end in tickets:
        routes[start] = routes.get(start, []) + [end]

    routes = sorted(routes, key = lambda x:x[1])

    stack =["ICN"]
    answer =[]
    while len(stack) >0:
        top = stack[-1]
        if top not in routes or len(routes[top]) ==0:
            answer.append(stack.pop(0))
        else:
            stack.append(routes[top].pop())

    return answer[::-1]


def solution(tickets):
    routes = {}
    for i in tickets:
        routes[i[0]] = routes.get(i[0], []) + [i[1]]

    for j in routes:
        routes[j].sort(reverse=True)

    stack = ["ICN"]
    answer = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    return answer[::-1]

