
'''
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
'''

def fibo_2748():

    num = int(input())
    num_list = []
    for i in range(0, num):
        N = int(input())
        num_list.append(N)

    def fibonacci(n):
        # 재귀적으로 선언된 fibonacci(0)과 fibonacci(1)을 횟수를 출력하는 함수
        if (n == 0):
            return [0]
        elif (n == 1):
            return [1]
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    for i in num_list:  # 입력으로 들어온 i에 대해
        list_fibo = fibonacci(i)  # 호출되는 fibonacci(0)과 fibonacci(1)을 값을 받아서
        num_0, num_1 = 0, 0

        for i in list_fibo:  # 1과 0을 세는 반복문
            if i == 1:
                num_1 = num_1 + 1  #
            else:
                num_0 = num_0 + 1

        print(num_0, num_1)  # 출력

    return

fibo_2748()