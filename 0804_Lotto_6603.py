# def lotto(x, cnt):
#     if cnt == 6:
#         for i in range(k):
#             if select[i]:
#                 print(a[i], end=' ')
#         print()
#         return
#
#     for i in range(x,k):
#         select[i]=1
#         lotto(x+1, cnt+1)
#         select[i]=0
#
# while True:
#     a = list(map(int, input().split()))
#     k =a[0]
#     if k ==0:
#         break
#     a =a[1:]
#     select =[0 for _ in range(k)]
#     lotto(0,0)
#     print()

# k, *num_li = list(map(int, input().split()))
# select = [0 for _ in range(k)]
# a =num_li[1:]
# def lotto(x, cnt):
#     if cnt ==6:
#         for i in range(k): #k는 전체 숫자 개수
#             if select[i]:
#                 print(a[i])
#         print()
#         return
#     for i in range(x,k):
#         select[1]=1
#         lotto(x+1, cnt+1)
#         select[i]=0



def dfs(x, cnt):
    if cnt == 6:
        for i in range(N):
            if visited[i]:
                print(num_li[i], end=' ')
        print()
        return

    for k in range(x,N):
        visited[k] = 1
        dfs(k+1, cnt+1)
        visited[k]=0

while(True):
    N, *num_li = list(map(int, input().split()))
    print(N)
    print(num_li)
    if N==0:
        break

    visited = [0 for i in range(N)]
    dfs(0,0)
    print(' ')




