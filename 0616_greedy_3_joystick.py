'''
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때,
이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
'''

name='JEROEN'
from collections import Counter

def solution(name):
    '''
    일단 제일 먼 글자를 입력해
    만약에 제일
    특정 문자 접근 가능한 방법이 두가지
    min(목표 인덱스 - 현재 인덱스, 현재 인덱스 + 마지막인덱스 순번)
    A는 제외 해야한다.
    맨처음에는 A
    '''
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = dict([(alpha[i],i) for i in range(len(alpha))])
    answer=[]
    current_idx =0

    for character in name:
        answer.append(min(alpha[character]+1, 25-alpha[character]))

    for i in range(len(name)):
        answer += min(abs(i - current_idx), len(name) - abs(i - current_idx))

    return answer

print(solution(name))
'''
def solution(name):
    count=0
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d={}
    indexes=[]
    current_idx=0

    for i in range(len(alpha)):
        d[alpha[i]]=min(i,26-i)

    for i in range(len(name)):
        num=d[name[i]] #
        count += num #해당 문자를 올리는데 사용한 조이스틱 횟수
        if num !=0 :
            indexes.append(i) #인덱스에 i번째 삽

    while True:
        if len(indexes)==0:
            break
            
        min_dist=99
        min_idx=0
        [0,1,2,3]
        for it in indexes: #모든 인덱스에 대해 수행한다.
            min_dist2=min(abs(it-current_idx),n-abs(it-current_idx))
            #현재 인덱스부터 정방향으로 갔을 때 vs 역방향으로 갔을 때

            if min_dist2 < min_dist:
                min_dist=min_dist2
                min_idx=it #인덱스를 바꿔준다.

        count+=min_dist
        indexes.remove(min_idx) #인덱스 제거
        current_idx = min_idx

    return count
'''
#이해 잘 안됨
def solution(name):
   m = [ min(ord(c)-65, 91-ord(c)) for c in name]
   #유니코드 변환함수 UNICODE 'A' : 65/ 'Z' : 90
   #뒤에서 접근했을 때 vs 원래 순으로 접근했을 떄
   #name에 대해 정방향/역방향을 비교해서 작은 값을 리스트에 저장
   answer = 0
   where = 0
   while True:
        answer += m[where] 
        m[where] = 0  #수행한 부분을 0으로 바꿔놓는다.
        if sum(m) == 0: #전체 합이 0이면 종료
            break

        left, right = (1,1)

        while m[where - left] <= 0: #수행했거나 'A'이거나
            left += 1

        while m[where + right] <= 0: #수행했거나 'A'이거나 #오른쪽으로
            right += 1

        answer += left if left < right else right #기본으로 정방향로 향한다. 조이스틱 횟수에는 +
        where += -left if left < right else right #위치는 -

    return answer

