def solution(arr):
    N= len(arr)
    dp_a = [1] + [0 for i in range(1,N)]
    dp_d_1 = [1]+[0 for i in range(1,N)]

    for i in range(1,N):
        dp_d = [1] + [0 for i in range(1, N)]
        if dp_a[i] == 0: dp_a[i]=1
        if dp_d[i] == 0: dp_d[i]=1
        asc = arr[:i]
        dsc = arr[i:][::-1]

        for j in range(i-1):
            if asc[i-1] > asc[j]:
                if dp_a[j]+1 > dp_a[j]:
                    dp_a[i] = dp_a[j] +1

        for j in range(len(dsc)):
            if dsc[0] > dsc[j]:
                if dp_d[j] + 1 > dp_d[i]:
                    dp_d[i] = dp_d[j] + 1
        dp_d_1[i]=max(dp_d)

    return dp_d[::-1]

arr=[1,5,2,1,4,3,4,5,2,1]

print(solution(arr))