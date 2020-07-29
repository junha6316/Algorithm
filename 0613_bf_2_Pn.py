'''
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
'''
import itertools
import itertools
def solution(numbers):
    li_num=[]
    for i in range(1,len(numbers)+1):
        li = itertools.permutations(numbers,i)
        for number in li:
            words = int("".join(number))# 아이디어
            li_num.append(words)

    for i in range(1,len(numbers)+1):
        li_num = set(map(int,map("".join, )))

    li_num=list(set(li_num))

    if 1 in li_num:
        li_num.remove(1)
    if 0 in li_num:
        li_num.remove(0)

    answer = len(li_num)
    for num in li_num:
        i = 1
        while(i<=num//2):
            if int(num) % i == 0 and (i != 1):
                answer -=1
                break
            i +=1

    return answer

numbers ="011"

print(solution(numbers))
#-----------------------다른 사람들 풀이----------------------------------------

from itertools import permutations
def solution(n):
    '''
    에라토스테네스의 체를 이용한 방
    '''
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
