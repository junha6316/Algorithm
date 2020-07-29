import sys
N = int(sys.stdin.readline())

num_li = list(map(int, sys.stdin.readline()[:-1].split()))
num_li.sort()
MAX = num_li[-1]
i=2
answer=[]
while(i<MAX):
    n=len(num_li)
    for idx in range(n):
        if num_li[idx]% i ==0 and num_li[idx] !=i:
            answer.append(idx)
    i+=1
answer = list(set(answer))
N -= len(answer)
for num in num_li:
    if num==1:
        N -=1

print(N)



