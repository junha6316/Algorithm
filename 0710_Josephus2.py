# import sys
# import queue
# N, k = map(int, sys.stdin.readline().split())
# answer=queue.Queue()
# arr=[]
# for i in range(N):
#     answer.put(i+1)
#
#
# while(answer.empty()== False):
#     for i in range(k-1):
#         answer.put(answer.get())
# #
# #     arr.append(str(answer.get()))
# #
# #
# # print(f"<{', '.join(arr)}>")
#
# # if k ==1:
# #     answer = arr
# # else:
# #     while(len(arr) > 0):
# #         for i in range(k-1):
# #             arr=  arr+[arr.pop(0)]
# #         answer.append(str(arr.pop(0)))
# #
# # print(f"<{', '.join(answer)}>")
#
# import sys
# import queue
#
# N, k = map(int, sys.stdin.readline().split())
# answer = queue.Queue()
# arr = []
# for i in range(N):
#     answer.put(i + 1)
#
# while (answer.empty() == False):
#     for i in range(k - 1):
#         a=answer.get()
#         answer.put(a)
#
#     arr.append(str(answer.get()))
#
# answer ='<' + ', '.join(arr) +'>'
# print(answer)
#
# from collections import deque
#
# def solution(N,k):
#     per =deque()
#     i=0
#     for i in range(1,N+1): per.append(i)
#     result='<'
#     while(len(per) !=0):
#         for i in range(k):
#             if i == k-1: result += str(per.popleft()) +', '
#             else:per.append(per.popleft())
#
#     return result[:-2] +'>'
#
# N, k = map(int, input().split())
# print(solution(N,k))

import sys
class SegTree:
    def __init__(self, n):
        size = 1
        while size < n: size <<= 1 #2의 제곱수로 증
        self.arr = [0] * (size * 2);
        self.size = size

    def construct(self, L):
        for i in range(len(L)):
            self.arr[self.size + i] = L[i]
        for i in range(self.size - 1, -1, -1):
            self.arr[i] = self.arr[2 * i] + self.arr[2 * i + 1]

    def update(self, i, val):
        i += self.size;
        self.arr[i] = val
        while i > 1: i //= 2; self.arr[i] = self.arr[i * 2] + self.arr[i * 2 + 1]

    def __getitem__(self, i):
        return self._kth(i, 1)

    def _kth(self, k, node=1):
        if node >= self.size: return node - self.size
        if k >= self.arr[node]: raise IndexError
        if k < self.arr[2 * node]: return self._kth(k, 2 * node)
        return self._kth(k - self.arr[2 * node], 2 * node + 1)

#
# n, m = map(int, input().split())
# game = SegTree(n)
# print(game.arr)
# game.construct([1] * n)
# print(game.arr)
# i = 0
# res = []
# for s in range(n, 0, -1):
#     i = (i + m - 1) % s
#     dead = game[i]
#     game.update(dead, 0)
#     res.append(dead + 1)
# print("<" + ", ".join(map(str, res)) + ">")




#
# from collections import deque
#
# def solution(N,k):
#     per =deque()
#     i=0
#     for i in range(1,N+1): per.append(i)
#     result='<'
#     while(len(per) !=0):
#         for i in range(k):
#             if i == k-1: result += str(per.popleft()) +', '
#             else:per.append(per.popleft())
#
#     return result[:-2] +'>'
#
# N, k = map(int, input().split())
# print(solution(N,k))


import sys

N, K = map(int, sys.stdin.readline().split())
circular_list = [i + 1 for i in range(N)]
answer = []
popNum = 0
answer = '<'
while len(circular_list) > 0:
    popNum = (popNum + (K - 1)) % len(circular_list)
    print(popNum)
    answer += str(circular_list.pop(popNum)) + ', '

print(answer[:-2] + '>')

































