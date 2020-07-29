from itertools import permutations
N=int(input())
num_li =list(map(int, input().split()))
num_li =list(permutations(num_li,N))
MAX =0
for case in num_li:
    answer =0
    for i in range(N-1):
        answer +=  abs(case[i] - case[i+1])
        if answer > MAX:
            MAX = answer

print(MAX)


while(True):
    a.pop(0)