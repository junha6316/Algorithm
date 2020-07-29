'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
1번 수포자 1,2,3,4,5
2번 수포자 2,1,2,3,2,4,2,5
3번 수포자 3,3,1,1,2,2,4,4,5,5
'''

def solution(answers):
    temp=[]
    answer=[0,0,0]
    tests=[[1,2,3,4,5],  #test[0]
        [2,1,2,3,2,4,2,5],   #test[1]
    [3,3,1,1,2,2,4,4,5,5]]  #test[2]

    for i in range(len(tests)):
        for j in range(len(answers)):  # 전체 답 인덱스
            if answers[j] == tests[i][j % len(tests[i])]:
                answer[i] += 1

    maxi=max(answer)
    for idx, sp in enumerate(answer):
        if maxi ==sp:
           temp.append(idx+1)

    return temp

answers=[1,3,2,4,2]
print(solution(answers))

#------다른 사람 풀이--------------------------------------------------------


from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]