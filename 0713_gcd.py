# import sys
# A, B = map(int, sys.stdin.readline()[:-1].split())
# def gcd(A,B):
#     gcd = min(A, B)
#     while (True):
#         r_A = A % gcd
#         r_B = B % gcd
#         if r_A == 0 and r_B == 0:
#            break
#         else:
#             gcd -=1
#
#
#     return gcd
#
# def lcf(A,B):
#     lcd=max(A,B)
#     while(True):
#         r_A = lcd % A
#         r_B = lcd % B
#         if r_A ==0  and r_B ==0:
#             break
#         else:
#             lcd += 1
#     return lcd
#
#
# print(gcd(A,B))
# print(lcf(A,B))

import sys

A, B = map(int, sys.stdin.readline()[:-1].split())


def gcd(A, B):
    while (B != 0):
        r = A % B
        A = B
        B = r

    return A


def lcm(A, B, gcd):
    return A * B / gcd


GCD = gcd(A, B)
LCM = lcm(A, B, GCD)

print(GCD)
print(LCM)


