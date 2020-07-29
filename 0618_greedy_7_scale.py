'''
문제 설명
하나의 양팔 저울을 이용하여 물건의 무게를 측정하려고 합니다.
 이 저울의 양팔의 끝에는 물건이나 추를 올려놓는 접시가 달려 있고, 양팔의 길이는 같습니다.
 또한, 저울의 한쪽에는 저울추들만 놓을 수 있고, 다른 쪽에는 무게를 측정하려는 물건만 올려놓을 수 있습니다.


저울추가 담긴 배열 weight가 매개변수로 주어질 때,
이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값을 return 하도록 solution 함수를 작성해주세요.

예를 들어, 무게가 각각 [3, 1, 6, 2, 7, 30, 1]인 7개의 저울추를 주어졌을 때,
이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21입니다.

제한 사항
저울추의 개수는 1개 이상 10,000개 이하입니다.
각 추의 무게는 1 이상 1,000,000 이하입니다.
'''
import queue

def solution(weights):
    weights.sort(reverse=True)
    i=1
    li=[]
    while(True):
        for weight in weights:
            if i >= weight:
                i -= weight
                li.append(weight)
                if i == 0:
                    i += sum(li)
                    break

            elif i <weight:
                pass

        if i !=sum(li):
            break

        i+=1
        li=[]

    return i + sum(li)


def solution(weight):
    weight.sort()
    ans = 1
    for e in weight: # 작은 거 부터 더해간다.
        if ans < e: #뽑은 값보다 정답이 작으면 멈춘다.
            break
        ans += e


    return ans


weight=[3, 1, 6, 2, 7, 30, 1]
weight=[1,1,2,3,6,7,30]

print(solution(weight))