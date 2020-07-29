# import
# def solution(left, right):
#     answer =0
#     i=0
#     while((len(left)!=0) || (len(right)!=0)):
#         l = left[0]
#         if  l > right[0]:
#             answer += right.pop(0)
#         else: #현재 l 값보다 오른쪽 카드값이 클떄
#             for j in range(0:)
#       return answer
#
#
# left = [3,2,5]
# right = [2,4,1]

'''
1. l 또는 l,r 둘다 버리면 얻는 점수 없음
2. r이 l보다 작을 때만 오른쪽 카드를 버리고 오른쪽 카드만큼 점수를 얻는다.
3. 한쪽을 다쓰면 게임 

'''

def solution(left, right):
    memo=[[0 for i in range(len(left)+1)] for i  in range(len(right)+1)]

    for i in range(len(right)):
        for j in range(len(left)):

            memo[i][j] = max(memo[i-1][j-1], memo[i-1][j] + right[j], memo[i][j-1])

    return memo

left = [3, 2, 5]
right = [2, 4, 1]

print(solution(left,right))