def DFS(student,visited):
    answer =0
    temp=[]
    def rDFS(i,temp):
        if visited[i] == False:
            visited[i]= True
            temp.append(i)
            rDFS(student[i],temp)

        else:
            if temp[0] != i:
                nonlocal answer
                answer+=1
                for i in range(1,len(temp)): visited[temp[i]] = False
            temp=[]

    for i in range(1, len(student)):
        if visited[i] == False:
            rDFS(i,temp)
            temp=[]

    return answer


def DFS(st
    udent,visited):
    answer =0
    temp=set()
    def rDFS(i, temp, visited):
        if i not in visited:
            visited.add(i)
            temp.add(i)
            rDFS(student[i], temp, visited)
        else:
            if list(temp)[0] != i:
                nonlocal answer
                answer+=1
                visited = visited - temp
            temp=set()

    for i in range(1, len(student)+1):
        if i not in visited:
            rDFS(i,temp,visited)
            temp=set()

    return answer

N= int(input())
for i in range(N):
    n= int(input())
    student = [0]+list(map(int, input().split()))
    visited=set()
    print(DFS(student, visited))



# import sys
#
# sys.setrecursionlimit(10**8)
#
# def dfs(idx, value, total_visited, visited):
#     if idx in total_visited:
#         return True, None
#
#     visited.add(idx)
#     total_visited(idx)
#
#     if value in visited:
#         global team
#         team +=1
#         return (idx == value), value
#
#     is_cycle, start_idx = dfs(value, students[value], visited, total_visited)
#
#     if is_cycle == False:
#         team += 1
#     if idx == start_idx:
#         is_cycle = True
#         return is_cycle, start_idx
#
# tc= int(sys.stdin.readline())
# for t in range(tc):
#     n= int(sys.stdin.readline())
#     students = list(map(int, sys.stdin.readline().split()))
#     team =0
#     visited =set()
#     for idx, value in enumerate(students):
#         if idx in visited:
#             continue
#         dfs(idx, value. set(), visited)

#
