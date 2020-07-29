# def stars(n):
#     matrix = []
#     for i in range(3 * len(n)):
#         if i // len(n) == 1:
#             matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
#         else:
#             matrix.append(n[i % len(n)] * 3)
#     return (list(matrix))
#
#
# star = ["***", "* *", "***"]
# n = int(input())
# k = 0
# while n != 3:
#     n = int(n / 3)
#     k += 1
#
# for i in range(k):
#     star = stars(star)
# for i in star:
#     print(i)
#
#
#
#
#
#
# def stars(n):
#     matrix =[]
#     N = len(n)
#     for i in range(3*N):
#         if i// N == 1:
#             matrix.append(n[i % N] + " " * N + n[i % N] )
#         else:
#             matrix.append(n[i% N] * 3)
#     return matrix
#
# star =["***","* *","***"]
# n= int(input())
# k=0
# while n !=3:
#     n= int(n/3)
#     k+=1
#
# for i in range(k):
#     star = stars(star)
#
# for i in star:
#     print(i)
#
#
#
#
#








def stars(star, X):
    N= len(star)

    if N== X:
        return star
    star = merge(star)
    return merge(star)

def merge(star):
    matrix =[]
    N=len(star)
    for i in range(3*N):
        if i // 3 ==1:
            matrix.append(star[i % N] + " "*N + star[i % N])
        else:
            matrix.append(star[i%N]*3)
    return matrix

star =["***","* *","***"]

for i in stars(star,27): print(i)
















