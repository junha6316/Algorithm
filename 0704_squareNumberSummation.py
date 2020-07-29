# def solution(num):
#     i = 1
#     if num == 1:
#         return 1
#     while (True):
#         if i ** 2 > num:
#             break
#         elif i ** 2 == num:
#             return 1
#
#         elif num % i ** 2 == 0 and i!=1:
#             return num // i ** 2
#
#         i += 1
#
#     return 1 + solution(num - ((i - 1) ** 2))
#
#
# N = int(input())
# print(solution(N))

#
# def solution(N):
#     dp=[0,1] + [0 for i in range(2,N+1)]
#     for i in range(2,N+1):
#         dp[i]=i
#         for j in range(1,i):
#             if j**2 > i: break
#             dp[i] =min(dp[i], dp[i-j**2]+1)
#     return dp
# N=int(input())
#
# print(solution(N))


def solution(N):
    dp = [0, 1] + [0 for i in range(2, N + 1)]
    for i in range(2, N + 1):
        dp[i] = i
        j = 1
        while (j ** 2 <= i)
            if dp[i] > dp[i - j ** 2] + 1:
                dp[i] = dp[i - j ** 2] + 1
            j += 1

    return dp[-1]


N = int(input())
print(solution(N))





