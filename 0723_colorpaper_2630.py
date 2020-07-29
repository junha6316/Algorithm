
# N= int(input())
# paper =[list(map(int, input().split())) for i in range(N)]

# def div(paper):
#     N=len(paper)
#
#     if N == 1:
#         return paper
#
#
#
#
#
#
#
# #     for i in range(N):
# #         for j in range(N):
# #             if paper[i][j] != paper[0][0]:
# #                 paper = div(paper)
# #
# #
# #
# #     paper =div(paper)
# #
# #     return merge(paper)
#
# paper = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#
# def div(paper):
#     N = len(paper) #8
#     if N == 1:
#         return paper
#
#
#     for i in range(N):
#         for j in range(N):
#             if paper[i][j] !=paper[0][0]:
#                 paper=sub(paper)
#
#     def sub(paper):
#         N=len(paper)
#         n = N // 2
#         result = []
#         for j in range(0,N,n):
#             for i in range(0,N,n):
#                 temp=[]
#                 for row in paper[i:i+n]:
#                     temp.append(row[j:j+n])
#                 result.append(temp)
#         return result
#
#
#     return temp
#
# for i in div(paper): print(i)
#
#
# from functools import reduce
#
#
# def cut(paper, x, y, size):
#     temp_paper = [paper[i][x:x + size] for i in range(y, y + size)]
#     flatten_paper = list(set(reduce(lambda x, y: x + y, temp_paper))) #w중복 제거
#
#     half = size//2
#     if len(flatten_paper) == 1:
#         result[flatten_paper[0]] += 1
#         return
#
#     dx =[0,half, 0, half]
#     dy = [0,0, half, half]
#
#     for i in range(4):
#         ux = x + dx[i]
#         uy = y + dy[i]
#         cut(paper,ux, uy, half)
#
#
# N = int(input())
# paper = [list(input().split()) for _ in range(N)]
# result = {'0': 0, '1': 0}
# cut(paper, 0, 0, N)
# print(f"{result['0']}\n{result['1']}")
#
#


def chk(paper):
    N=len(paper)
    if N== 1:
        return True
    for i in range(N):
        for j in range(N):
            if paper[i][j] != paper[0][0]:
                return False
    return True

def cut(paper,x ,y, size):
    temp_paper = [paper[i][x:x+size] for i in range(y,y+size)]
    check=chk(temp_paper)
    half = size//2

    if check:
        result[temp_paper[0][0]] +=1
        return

    dx = [0, half, 0, half]
    dy = [0, 0, half, half]

    for i in range(4):
        ux = x + dx[i]
        uy = y + dy[i]
        cut(paper,ux, uy, half)

N = int(input())
paper = [list(input().split()) for _ in range(N)]
result = {'0': 0, '1': 0}
cut(paper, 0, 0, N)
print(f"{result['0']}\n{result['1']}")




