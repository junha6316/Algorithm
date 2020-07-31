'''

LRU : 가장 최근에 사용된 적이 없는 캐시의 메모리부터 대체하며

'''
from collections import deque

def solution(cashsize,cities):
    if cashsize ==0:
        return len(cities)*5

    cashes=deque()
    answer =0

    for city in cities:
        isInCash = False
        city = city.upper()
        if len(cashes) < cashsize:
            cashes.append([1,city])
            answer += 5
            continue

        for cash in cashes:
           if cash[1] == city:
               isInCash = True
               cash[0] += 1
               answer +=1
               break

        if not isInCash:
            answer += 5
            cashes.popleft()
            cashes.append([1, city])
        else:
            cashes = deque(sorted(cashes, key =lambda x:x[0]))
            print(cashes.popleft())
    print(cashes)



    return answer



cashSize = 3
cities =	['Jeju', 'Pangyo', 'NewYork', 'newyork']
print(solution(cashSize, cities))