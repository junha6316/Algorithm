'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

입력
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

N= int(input())

시작시간 :8:43
Seq= list(map(int, input().split()))

ai > ai-1

1. 증가해야한다  ai > ai-1
2. 가장 길어야한다.

2개
0   0   0  0   0  50
0   0   0  30  0  0
0   20  0  0   20 0
10  0  10  0   0  0

증가하는 수열
         6  7 1 2 3 4 5
memo[1] 10 20 1 2 3 4 5

0 20  0  0  0  0  5
10 0  0  0  0  4  0
0  0  0  0  3  0  0
0  0  0  2  0  0  0
0  0  1  0  0  0  0

10 20              10 20
10 20 10           10 20
10 20 10 30        10 20 30
10 20 10 30 20     10 20 30
10 20 10 30 20 50  10 20 30 50

1 10 2              / 1 10 , 1 2
1 9 10 2 20           / 1 9 10 20,
1 9 10 2 20        / 1 10 20 30, 1 2 20 30

가장 마지막에 있는 값중에 가장 큰

수열의 길이가 N의 최대 길이는
[1, 2, 3, 4, 5,.., n]
N= int(input())
Seq= list(map(int, input().split()))


https://dyngina.tistory.com/16

'''

      #[1 10 2 20 3 10 4 30 5 20 6 50]
       # 1   2   1   3   2   4
Seq = [10, 20 ,10, 30, 20, 50]

      # 2   1   3  2    5   4  4
#Seq = [1,10,2,20,3,30,4,40,5,50,6,7]

N= len(Seq)

N= int(input())
Seq= list(map(int, input().split()))
dp=[0 for i in range(len(Seq))]

for i in range(0,N-1): #N부터 0까지
    i = (N-1)-i #N-1, N-2, .., 1
    a = 1
    if i == N-1:
        max1=Seq[-1]
        for j in range(1,N):
            if Seq[N-1-j] < max1:
                   a += 1
                   max1 = Seq[N-1-j]
            else:
                pass
        dp[-1] = a
    else: #N-2, N-3
        max1 = Seq[i]
        for j in range(2, i):
            if Seq[N-1-j] < max1:
                   a += 1
                   max1 = Seq[N-1-j]
            else: pass
            dp[i] = max(a,dp[i+1])
print(dp)

'''
https://shoark7.github.io/programming/algorithm/3-LIS-algorithms
여기를 참고 했다.
Lis는 다음과 같은 규칙을 따른다.

1.정수 i, j에 대해 i < j이면, S[i] < S[j]다.(0 <= i, j <= |S|)
2.정수 i, j에 대해 S[i] < S[j]이면, 원 배열 arr에서의 S[i], S[j] 
두 수의 위치 전후관계는 같다.(0 <= i, j <= |S|)

1. 완전 탐색의 경우(시간 복잡도 : 2^N)

def LIS_bf(arr):
    
    if not arr:
        return 0
        
    ret =1
    for i in range(len(arr)): #LIS의 시작 숫자 i를 선택한다.
        nxt =[]
        for j in range(i+1, len(arr)): # i를 제외한 리스트의 마지막까지 탐색
            if arr[i] < arr[j]:        # 만약 j번째 원소가 i번째보다 크다면
                nxt.append(arr[j])      # nxt에 j번째 원소를 추가한다.
        ret=max(ret, 1+LIS(nxt))) #1과 LIS(nxt)를 돌림  재귀적으로 선언되어 있음
    retrurn ret
    
    
    
2. 동적계획법 (시간 복잡도 : N^2)
    
    def LIS_dp(arr):
        N = len(arr)
        dp =[-1] * N #메모이제이션을 위한 초기화
        
        def find(start):
            if dp[start] != -1
                return dp[start] #dp[i]가 초기화 상태가 아니면 그대로 반환
            
            ret = 1
            for nxt in range(start+1,N): #start+1에서 시작해서 arr의 마지막 원소까지
                if arr[start] < arr[nxt]: #arr[nxt]의 원소가 arr[start]보다 크면
                    ret=max(ret, find(nxt)+1) # ret
                    
            dp[start] =ret #이전 값과 다음 값 중 큰 값을 할당 
            return ret
            
        return find(0)
        
3. 이진 탐색을 통한 최적화
    # 이진 탐색 공부 후 다시볼 
    # https://shoark7.github.io/programming/algorithm/3-LIS-algorithms것
   
    기본 아이디어는 원소가 N개 리스트의 앞쪽부터 탐색한다 가정했을 때
    k(k<N)개 탐색할 때 길이가 동일한 LIS가 존재함
    그 중 마지막 값이 가장 작은 LIS가 이후 탐색에서 길이가 가장 긴 LIS가 될 
    확률이 높다.
    가령 A =[5,6,1,2,...]이라는 리스트에서 4번째 탐색을 가정해보면
    [5,6,1,2]에 대해서 부분 LIS를 구하면 [5,6], [1,2]가 있다.
    [5,6]의 마지막 원소의 값은 6/ [1,2]의 마지막 원소의 값은 2이다.
    이 둘 중 전체 리스트에서 LIS가 될 확룰이 높은 부분 LIS는 [1,2]이다.
    즉 같은 크기의 증가 수열에서 마지막 값이 최소인 부분 수열을 기억하면 된다. 
    
    
'''







