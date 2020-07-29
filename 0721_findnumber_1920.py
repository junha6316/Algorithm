

# def BTS(num_list,n):
#     i = len(num_list) // 2
#
#     if num_list[i] < n:
#         if len(num_list) == 1: return 0
#         else: return BTS(num_list[i+1:],n)
#
#     elif num_list[i] > n:
#         if len(num_list) == 1: return 0
#         else: return BTS(num_list[:i],n)
#
#     elif num_list[i] == n:
#         return 1

# import sys
# N= int(input())
# num_list = list(map(int, sys.stdin.readline().split()))
# num_list.sort()
#
# n = int(input())
# f_li = list(map(int, sys.stdin.readline().split()))
# sys.setrecursionlimit(10**9)
def BTS(target, start, end, data):
    if start > end:
        return 0

    mid = (start + end) // 2

    if data[mid] == target:
        return 1

    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return BTS(target, start, end, data)

f_li=[i+1 for i in range(0,10000)]
num_list = [i+1 for i in range(0,10000)]

n= 10000
for i in range(n):
    print(BTS(f_li[i], 0, n-1, num_list))


