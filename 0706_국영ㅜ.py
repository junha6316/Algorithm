import sys
def solution(N, arr):
    arr=[[arr[i][0], int(arr[i][1]),int(arr[i][2]), int(arr[i][3])] for i in range(N)]

    arr= sorted(arr, key=lambda x:x[0])
    arr= sorted(arr, key=lambda x:x[3], reverse=True)
    arr= sorted(arr, key=lambda x:x[2])
    arr= sorted(arr, key=lambda x:x[1], reverse=True)

    for i in arr:
        print(f'{i[0]}')
    return



N=int(sys.stdin.readline())
arr= [sys.stdin.readline().split() for i in range(N)]

solution(N,arr)