'''
n개의 정수로 이루어진 임의의 수열이 주어진다.
 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.

단, 수는 한 개 이상 선택해야 한다.
예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
첫째 줄에 답을 출력한다.
________________________________________________________________________________________
가장 큰 수부터 시작해서

Si = Si + ai
10, -4, 3, 1, 5, 6, -35, 12, 21, -1
[19  9   13   10  9   4   -2  33   21    20 ]
________________________________________________________________________________
1. 가장 큰 값을 찾는다,

시작시간 20/05/16 16:00

num = int(input())
N_list = list(map(int, input().split()))
2, 1, -4, 3, 4, -4, 6, 5, -5, 1
 3  -3  -1  7  0  2  11  0  -4
   -1  0  3 -4  6  7  6  1
     2  4  -1  9 11 2  7
      6   0  5 14 6

a0,        ,an
'
import time
시간
'''
#

#N_list=[i for i in range(-10,10)]
#num=len(N_list)
#N_list=[2, 1, -4, 3, 4, -4, 6, 5, -5, 1] [ 3 -4 7 -4 11 -5 1]
'''
dp[i] 원소의 개수가 i개 일 때 최소 합
[2] : 2 [                               [2]
[2 1] :3                                [2,1] ,[1]
[2 1 -4] : 3   1개 추가되서 생기는 경우의 수   [2,1-4], [1,-4] [-4]
[2 1 -4 3] : 3 1개 추가되서 생기는 경우의 수 : [2,1,-4,3] [1,-4,3] [-4,3] [3] 4
[2 1 -4 3 4] : 7                      : [2 1 -4 3 4] [1-4 3 4] [-4 3 4] [3 4] [4] 5 [3 -4 7]

N개 N(N+1)/2
'''

#sum=0
#N = int(input())
#N_list = list(map(int, input().split()))
N_list=[2, 1, -4, 3, 4, -4, 6, 5, -5, 1]
       #[2, 3, 3, 6, 10, 10, 16, 21, 21, 22]
#N_list=[10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
       #[10, 10, 10, 11, 16, 22, 22, 22, 43, 43]
#N_list=[i for i in range(-10,10)]


N= 10
dp =[0 for j in range(N)]
minus=0
'''
dp[n] = dp[n] + dp[n-1]
n번째 이전의 합과 n번째 수를 더하면 n번째까지의 합
출처: https://mygumi.tistory.com/97 [마이구미의 HelloWorld]
1. dp[i-1] > 0
  - 이전의 합이 음수라면 선택할 필요 없이 현재부터 다시 선택해나가면 된다. 
2. dp[i] + dp[i-1] > 0
  - 이전의 합과 현재의 수를 더한 값이 음수라면 선택할 필요가 없다. 
출처: https://mygumi.tistory.com/97 [마이구미의 HelloWorld]

for(int i=2;i<=n;i++) {


    if (dp[i-1] > 0 && dp[i] + dp[i-1] > 0) {
        dp[i] += dp[i-1];
    } 

    if (max < dp[i]) {
        max = dp[i];
    }

}

'''
N = int(input())
dp = list(map(int, input().split()))
for i in range(0, N):
    if dp[i-1] <0 or N_list[i]+dp[i-1]<0:
        pass
    else:
        dp[i] = dp[i] + dp[i-1]



print(dp)

'''
def contiSum(arr):
    dp =[0.1] * N
    def find(start):
        if dp[start] != 0.1:
            return dp[start]
        sum = 0
        for nxt in range(start + 1, N):  # start+1에서 시작해서 arr의 마지막 원소까지
            # arr[nxt]의 원소가 arr[start]보다 크면
            sum = max(sum, find(nxt) + arr[nxt])
        dp[start] = sum  # 이전 값과 다음 값 중 큰 값을 할당
        return sum
    return find(0)

print(contiSum(N_list))


    def LIS_dp(arr):
        N = len(arr)
        dp = [-1] * N  # 메모이제이션을 위한 초기화

        def find(start):
            if dp[start] != -1
                return dp[start]  # dp[i]가 초기화 상태가 아니면 그대로 반환

            ret = 1
            for nxt in range(start + 1, N):  # start+1에서 시작해서 arr의 마지막 원소까지
                if arr[start] < arr[nxt]:  # arr[nxt]의 원소가 arr[start]보다 크면
                    ret = max(ret, find(nxt) + 1)  # ret

            dp[start] = ret  # 이전 값과 다음 값 중 큰 값을 할당 
            return ret

        return find(0)


def conv(arr):
    # 리스트내에 연속된 양수, 또 음수가 있을 때 모두 더해준 리스트를 반환하는 함
    sum=0
    sum1=[]
    for i in range (0,len(arr)-1):
        if i == len(arr)-2:
            if (sum*arr[i+1]) >= 0:
                sum += arr[i+1]
                sum1.append(sum)
                return sum1
            elif (sum*arr[i+1]) < 0:
                sum1.append(sum)
                sum1.append(arr[i+1])
                return sum1
        else:
            if arr[i] >=0:
                sum += arr[i]
                if arr[i+1] >=0:
                    pass
                else:
                   sum1.append(sum)
                   sum=0

            elif arr[i] <0:
                sum += arr[i]
                if arr[i + 1] <= 0:
                    pass
                else:
                    sum1.append(sum)
                    sum=0
            else:
                pass

def conv(arr):
    # 리스트내에 연속된 양수, 또 음수가 있을 때 모두 더해준 리스트를 반환하는 함
    sum=0
    sum1=[]
    for i in range (0,len(arr)-1):
        if  i == 0: sum += arr[0]
        else:
            if arr[i] >= 0 and  arr[i+1] >=0:
                sum += arr[i]
            elif arr[i] >0 and arr[i+1] <= 0:
                sum += arr[i]
                sum1.append(sum)
                sum=0
            elif arr[i] < 0 and  arr[i+1] <0:
                sum += arr[i]
            elif arr[i] < 0 and  arr[i+1] >0:
                sum += arr[i]
                sum1.append(sum)
                sum = 0
            else:
                pass
    return sum1



print(conv(N_list))
'''





#print(sum1)









#음수 양수를 먼저 계산 해놓고 해보자


'''
N_lst=sum1
print(sum1)

#num = int(input())
#N_list = list(map(int, input().split()))

Maxi = max(N_list)
for i in range(0,num):
    if i == 0:
        memo = [[0 for i in range(0, num)], [0 for i in range(0, num-1)]] #[[n-1 시행], [n 시행]]
        memo[0] = N_list
    else:
        memo[1] = [0 for i in range(0,len(memo[0])-1)]
        for j in range(0, num-i):  # 1층 일때 0 ~ num-2 9
            memo[1][j] = memo[0][j] + N_list[j+i]
        if max(memo[1]) > Maxi: Maxi = max(memo[1])
        else:
            pass
        memo[0] = memo[1]

        print(Maxi)



N_list=[2, 1, -4, 3, 4, -4, 6, 5, -5, 1]
      #[+  +  -   +  +  -   +  +  -   +]
sum1=[]
sum=0
for i in N_list:
    if i>0:
        sum += i
    else:
        sum1.append(sum)
        sum1.append(i)
        sum=0
print(sum1)






memo = [0 for i in range(0, len(N_list))]

num=len(N_list)

for i in range(0,len(N_list)):
    memo[i-1] = N_list[i-1]+N_list[i]
    
print(memo)


#print(memo)
#memo[1][j] = memo[0][j - 1] + N_list[j + i]


    #print([len(memo[0]),len(memo[1])])



    
    

print(memo)


#print(time.time()-start)
#memo[i]= memo[i-1]+N_list[i]
'''










