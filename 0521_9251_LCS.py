'''

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP일와 CAPCAK의 LCS는 ACAK가 된다.
원소의 순서가 같아야함
동일한 값이 들어오면 dp[i] =dp[i-1]+1
ex)
AC'T'
CA'T'
다른 값이 들어오면 각 들어온 원소를 상대 리스트에서 검색 수행 후
인덱스 기준으로 판
있으면 +1단?>

CAPT
CPA

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다.
문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
인덱스가 크거나 같으면서 문자가 동
출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
li_A = list(input())
li_B = list(input())

모르겠다.


'''
#li_A = list('ACAYKP')
#li_B = list('CAPCAK')

li_A = list(input())
li_B = list(input())

dp=[[0 for i in range(len(li_B))] for i in range(len(li_A))]

for i in range(1,len(li_B)):
    for j in range(0,len(li_A)):
        if li_B[i] == li_A[j]:
                dp[i][j] = dp[i-1][j-1] + 1
        else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp)

