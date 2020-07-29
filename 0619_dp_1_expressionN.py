'''
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5
60 =
5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.

+ - / *
// 괄호
5사용 횟수
1. N에 도달하는 방법을 찾는 함수
- 가장 빠르게 도달하는 방법 55,555,5555,
- 동일 연산일 경우 괄호로 묶어준다.
55, 555,
5*5 5*5*5
 '5/5' * number % N
 number//N * '5+'

 File -> Settings -> Editor -> General -> Appearance -> uncheck the option "Show hard wrap guide"



'''


def solution(N, number):

    dp = ['5']*(number//N) +['5/5']*(number%5)
    i=0
    while(True):
        if dp.count(str(N)) >= 2 and dp.count(str(N) + '/'+str(N)) >=1:
            dp.remove('5')
            dp.remove('5')
            dp.remove('5/5')
            dp.append('55/5')
        i+=1
        if i==1:
            break

    return dp
# 다른사람 풀이

 def solution(N, number):
        S = [{N}]
        for i in range(2, 9):
            lst = [int(str(N) * i)] #[55,555,5555,...,55555555]
            for X_i in range(0, int(i / 2)): #자릿수의 절반
                for x in S[X_i]:
                    for y in S[i - X_i - 2]:
                        lst.append(x + y)
                        lst.append(x - y)
                        lst.append(y - x)
                        lst.append(x * y)
                        if x != 0: lst.append(y // x)
                        if y != 0: lst.append(x // y)

            if number in set(lst):
                return i
            S.append(lst) #for문을 돌면서 값을 추가한다.
        return -1

 '''
 5를 1번 사용해서 만들 수 있는 수
 5
 =>SET 1
 5를 2번 사용해서 만들 수 있는 수
 55/ 5를 연속해서 이어 붙인 수
 10(5+5) 0(5-5) 25(5*5) 1(5/5) //사칙연산 결과
 => SET 2
 
 5를 3번 사용해서 만들 수 있는 수
 555
 (SET 1과 SET 2를 사칙연산한 결과) U (SET 2와 SET 1을 사칙연산한 결과) 
 => SET 3
 3 = 2+1 = 1+2
 
 5를 4번 사용해서 만들 수 있는 수
 5555
 (SET 1과 SET 3를 사칙연산한 결과) U (SET 2와 SET 2을 사칙연산한 결과) U (SET 3와 SET 1을 사칙연산한 결과) 
 
 4=3+1=2+2=3+1
 
 +,* 연산은 자리가 바뀌어도 같은값이지만 -/연산은 자리가 바뀌게 되면 다른 수 
 '''


N=5
number=12

print(solution(N,number))