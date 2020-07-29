from itertools import combinations
from operator import itemgetter

def solution(number, k):
    '''
    시간 초과 났
    '''
    li_num = list(combinations(number, len(number) - k))
    maxi=max(number)
    for idx, num in enumerate(li_num):
        if num[0] != maxi:
            del li_num[idx]


    for i in reversed(range(len(number)-k)):
         li_num =sorted(li_num, key=itemgetter(i),reverse=True)

    return ''.join(li_num[0])

#다시 해보기
#자리가 상관있기 때문에 이렇게 해도 된다
def solution(number, k):
    li = [[number[0]]]
    for num in number[1:]:
        while len(li)>0 and num> li[-1] and k>0: #이번에 뽑은 숫자가 크면
            li.pop() #맨 끝의 원소를 제거하고 그걸 첫째 자리로 사용한
            k -= 1
        li.append(num) #추가
    if k!=0:
        li = li[:-k] #뒷자리를 잘라주는 역할 "987654321"이런 경우 이런 경우에는 k가 안깎이고 왔기 때문에 자리수를 잘라야한다.

    return ''.join(li)


#-------------------------다른 사람 풀이------------------------
def solution(number, k):
    stack = [number[0]] #첫번쨰 자리를 넣어준다.
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            '''
            stack의 마지막 원소가 현재 뽑은 원소보다 작으면 뺸다는건데
            stack을 완전히 비우거나
            k 의 원소를 제거하거나
            '''
            k -= 1
            stack.pop() #맨 뒤 원소를 제거
        stack.append(num) #num을 뒤에 추가한다.
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

number = "1492"
k=2
print(solution(number,k))
