import sys
I= int(sys.stdin.readline())

arr=[list(sys.stdin.readline().split()) for i in range(I)]
arr=[[i, int(arr[i][0]), arr[i][1]] for i in range(I)]

arr=sorted(arr, key=lambda x:x[0])
arr=sorted(arr, key=lambda x:x[1])

for item in arr:
    print(f'{item[1]} {item[2]}')