'''
자카드 유사도
: 두집합의 교집합의 크기를 합집합의 크기로 나눈 값
단일 집합 다중집합(원소의 중복으 허용하는 집합)

문자열에도 적용가능
대문자 소문자 차이 무시
기타 공백, 숫자, 특수문자가 들어있는 경우 글자쌍을 버린다.

'''
import re
from collections import Counter

def solution(str1, str2):
    if not str1.isupper(): str1 = str1.upper()
    if not str2.isupper(): str2 = str2.upper()

    set_1=[]
    set_2=[]
    for idx in range (len(str1)-1):
        text = str1[idx:idx+2]
        text = re.sub('[^A-Z]', '', text).strip()
        if len(text) == 2:
            set_1.append(text)


    for idx in range (len(str2)-1):
        text = str2[idx:idx + 2]
        text = re.sub('[^A-Z]', '', text).strip()
        if len(text) == 2:
            set_2.append(text)

    print(set_1)
    print(set_2)

    set_1 = Counter(set_1)
    set_2 = Counter(set_2)
    intersec = set_1& set_2
    uni = set_1 | set_2

    if len(list(uni.elements())) !=0:
        return int(len(list(intersec.elements())) / len(list(uni.elements()))*65536)
    else:
        return


str1= 'FRANCE'
str2 = 'french'

str1 =	"E=M*C^2"
str2= "e=m*c^2"
print(solution(str1, str2))
