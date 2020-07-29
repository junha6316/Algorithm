# import sys
# import heapq as hq
# N = int(sys.stdin.readline())
# li=[]
# for i in range(N):
#     num = int(sys.stdin.readline())
#     if num==1:
#         print(1)
#     else:
#         hq.heappush(li, num)
#
# for i in li:
#     print(hq.heappop(li))

import sys

N = int(sys.stdin.readline())
li=[0 for i in range(10000)]
for i in range(N):
    num = int(sys.stdin.readline())
    li[num] += 1

for i in range(10000):
    if li[i] ==0:
        pass
    else:
        for j in range(li[i]):
            print(i)
