#
# N= int(input())
# cor = [tuple(map(int, input().split())) for i in range(N)]
# cor.sort()
#
# def distance(cor):
#     N=len(cor)
#     small = 9999999999
#     for i in range(N):
#         for j in range(i+1,N):
#             dx = cor[i][0] - cor[j][0]
#             dy = cor[i][1] - cor[j][1]
#
#             l = dx*dx + dy*dy
#             if l < small:
#                 small = l
#     return small
#
#
# def divide(cor):
#     if len(cor) ==2:
#         return distance(cor), cor
#     else:
#         st = 0
#         end = len(cor)
#         mid =(st+end)//2
#
#         left = cor[:mid]
#         right =cor[:mid]
#
#         l_l, left = divide(left)
#         l_r, right = divide(right)
#
#         ll = min(l_l,l_r, distance([left[-1],right[0]]))
#
#         return  ll, left+right
#
# print(divide(cor)[0])


N= int(input())
cor = [tuple(map(int, input().split())) for i in range(N)]
cor.sort()
import sys
sys.setrecursionlimit(10*7)
def distance(cor):
    N=len(cor)
    small = 9999999999
    if N== 1:
        return small


    for i in range(N):
        for j in range(i+1,N):
            dx = cor[i][0] - cor[j][0]
            dy = cor[i][1] - cor[j][1]

            l = dx*dx + dy*dy
            if l < small:
                small = l
    return small


def divide(cor):
    N= len(cor)
    if N ==3 or N ==2:

            return cor, distance(cor), cor[0], cor[-1]
    else:
        st = 0
        end = len(cor)
        mid =(st+end)//2

        left = cor[:mid]
        right =cor[mid:]

        left, l_l, ll, lr = divide(left)
        right, l_r, rl, rr = divide(right)
        print(left)
        print(right)

        ll = min(l_l,l_r, distance([lr,rl]))

        if len(left) ==0:
            return [],ll, right[0], right[-1]

        elif len(right) ==0:
            return [], ll, left[0], left[-1]

        else:
            return [],ll, left[0], right[-1]



print(divide(cor)[1])









