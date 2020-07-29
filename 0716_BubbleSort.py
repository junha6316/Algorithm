N= int(input())
num_li = list(map(int, input().split()))

def solution(num_li):
    swap =0

    def conquer(left, right):
        result = []
        while (len(left) > 0 and len(right) > 0):
            if left[0] > right[0]:
                result.append(right.pop(0))
                nonlocal swap
                swap += 1
            else:
                result.append(left.pop(0))

        if len(left) > 0:
            result.extend(left)
        if len(right) > 0:
            result.extend(right)

        return result

    def div(li):
        if len(li) ==1: return li
        mid = len(li)//2

        left = li[:mid]
        right = li[mid:]

        left = div(left)
        right = div(right)

        return conquer(left, right)

    div(num_li)

    return swap

print(solution(num_li))


#
# t=0
# swap=0
# answer=[]
# while(t<N):
#     for i in range(N-1-t):
#         if num_li[i] > num_li[i+1]:
#             temp = num_li[i]
#             num_li[i] = num_li[i+1]
#             num_li[i+1] = temp
#             swap+=1
#         else:
#             pass
#     t+=1
#
# print(swap)