# import sys
def primelist(N):
    isPrime =[True] *N
    for i in range(2,N+1):
        if i *i > N: break
        if isPrime[i]:
            for j in range(i+i, N , i):
                isPrime[j] = False

    return isPrime
prime = primelist(1000000)
#
# while(True):
#     N= int(sys.stdin.readline())
#     if N ==0:
#         break
#
#     for i in range(2, MAX + 1):
#         if prime[i] is False:
#             j = n - i
#             if prime[j] is False:
#                 print(n, "=", i, "+", j)
#                 break
#

def primelist(N):
    isPrime =[True] *N
    for i in range(2,N+1):
        if i *i > N: break
        if isPrime[i]:
            for j in range(i+i, N , i):
                isPrime[j] = False

    return isPrime
prime = primelist(1000000)
print(len(prime))
#
def Primelist(n):
    num_li=[0,0]+[i for i in range(2,n+1)]
    i=2
    for i in range(2, n+2):
        if i*i > n : break
        if num_li[i] != 0:
            for j in range(i+1, n, i):
                num_li[i] = 0

    return num_li
primeli = Primelist(1000000)
print(len(primeli))

# while(True):
#     N = int(input())
#     if N == 0: break
#
#     for prime in primeli:
#         if primeli[N - prime] !=0 and prime != 0:
#             print(N, "=", prime, "+", N-prime)
print(len(primeli))





N =int(input())






