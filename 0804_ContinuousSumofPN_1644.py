N = int(input())
prime=[True for i in range(2,N+1)]
prime= [False, False] +prime
answer =0
for i in range(2, int(N**0.5)):
    if prime[i] ==True:
        for j in range(2*i,N+1, i):
            prime[j] = False

left, right =0,0
S=0
prime =[i for i in range(N+1) if prime[i]]
M=len(prime)
print(M)
print(prime)
while True:
    print(left, right, answer)
    if S >= N:
        if S == N:
            answer += 1
        S -= prime[left]
        left += 1

    else:
        if right == M:
            break
        S += prime[right]
        right += 1

print(answer)




