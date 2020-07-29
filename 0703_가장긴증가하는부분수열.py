#
# N=len(arr)
#
# N = int(input())
# arr=list(map(int, input().split()))
#
#
# dp=[1]+[0 for i in range(1,N)]
# for i in range(N):
#     if dp[i] ==0: dp[i]=1
#     for j in range(i):
#         if (arr[i]> arr[j]):
#             if(dp[i]<dp[j]+1):
#                 dp[i] =dp[j]+1
# print(dp)

arr = [10,100,50,20,30]

def solution(arr):
    i_dp=[[arr[0], arr[1], 1]] # start, end, length

    for i in range(0, len(arr)):
        for index in i_dp:
            if arr[i] < i_dp[0][0]:
                i_dp = [[arr[i],arr[i],1]] + i_dp
                break
            elif arr[i] >index[1]:
                index[2] += 1
                index[1] = arr[i]
            elif arr[i] >index[0] and arr[i] <index[1]:
                i_dp.append([index[0],arr[i],2])

    i_dp=sorted(i_dp, key=lambda x:x[2], reverse= True)
    print(i_dp[0][2])

    return i_dp

print(solution(arr))

# N= int(input())
# arr=list(map(int, input()))
# i_dp=[[arr[0], arr[1], 1]] # start, end, length
#
# for i in range(0, len(arr)):
#     for index in i_dp:
#         if arr[i] < i_dp[0][0]:
#             i_dp = [[arr[i],arr[i],1]] + i_dp
#             break
#         elif arr[i] >index[1]:
#             index[2] += 1
#             index[1] = arr[i]
#         if arr[i] >index[0] and arr[i] <index[1]:
#             i_dp.append([index[0],arr[i],2])
#
# i_dp=sorted(i_dp, key=lambda x:x[2], reverse= True)
# print(i_dp[0][2])





























