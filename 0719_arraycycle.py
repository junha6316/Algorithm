'''
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
'''
import sys
N=int((sys.stdin.readline()))

for i in range(N):
    n= int((sys.stdin.readline()))
    arr =[0] +list(map(int, sys.stdin.readline().split()))
    answer=0
    visited=[True]+[False for i in range(n)]
    for i in range(1, n+1):
        if visited[i]: continue
        visited[i] = True
        a=arr[i]
        while(visited[a] ==False):
            visited[a] = True
            a=arr[a]
        answer += 1
    print(answer)


#
# import sys
#
#
# sys.setrecursionlimit(10 ** 6)
#
# def read_list_int():
#     return list(map(int, sys.stdin.readline().strip().split(' ')))
#
# def read_single_int():
#     return int(sys.stdin.readline().strip())
#
# def get_permutation_count(l, N):
#     visits = [False for _ in range(N+1)]
#     count = 0
#     for i in range(1, N+1):
#         if visits[i]:
#             continue
#         visits[i] = True
#         n = l[i]
#         while not visits[n]:
#             visits[n] = True
#             n = l[n]
#         count += 1
#     return count
#
#
# if __name__ == '__main__':
#     T = read_single_int()
#     for _ in range(T):
#         N = read_single_int()
#         l = read_list_int()
#         print(get_permutation_count([0]+l, N))
#
#
#
