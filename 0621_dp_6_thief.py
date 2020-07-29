# def solution(a):
#     x1, y1, z1 = a[0], a[1], a[0]+a[2]
#     x2, y2, z2 = 0, a[1], a[2]
#
#     for i in a[3]:
#         x1, y1, z1 = y1, z1, max(x1, y1) +i
#         x2, y2, z2 = y2, z2 , max(x2, y2)+i
#     return max(x1, y1, y2, z2)



def solution(money):
    dp1=[0 for i in range(len(money)-1)] #첫번째 집을 털었을 때 length-1 까
    dp2=[0 for i in range(len(money))]#첫번쨰 집을 털지 않았을 때

    dp1[0] = money[0]
    dp1[1] = money[0]

    dp2[0] = 0
    dp2[1] = money[1]

    for i in range (2,len(money)-1):
        dp1[i] = max(dp1[i-2] +money[i],dp1[i-1])

    for i in range(2,len(money)):
        dp2[i]=max(dp2[i-2]+money[i], dp2[i-1])

    return dp1

money = [1,2,3,1]

print(solution(money))
