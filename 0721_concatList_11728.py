# N, M = map(int, input().split())
#
# A = list(map(int, input().split()))
# B= list(map(int, input().split()))
#
# result=[]
#
# while(len(A) != 0 and len(B) != 0):
#     if A[0] >= B[0]:
#         result.append(str(B.pop(0)))
#     else:
#         result.append(str(A.pop(0)))
#
#
# if len(A) >0:
#     for i in A:
#         result.append(str(i))
#
# if len(B) >0:
#     for i in B:
#         result.append(str(i))
#
# print(' '.join(result))


N, M = map(int, input().split())

A = list(map(int, input().split()))
B= list(map(int, input().split()))

result = A+B
result.sort()
result  =[str(i) for i in result]
print(' '.join(result))

import time
a=[i+1 for i in range(10000000)]
b=[]
for i in range(a):
    if i 