import sys
def solution(N,k):
    arr= list(map(int ,sys.stdin.readline().split()))
    arr.sort()
    return arr[k-1]

N, k =map(int, sys.stdin.readline().split())
print(solution(N,k))