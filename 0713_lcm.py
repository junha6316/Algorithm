import sys

def gcd(A,B):
    while(B!=0):
        r = A % B
        A = B
        B = r
    return A

N= int(sys.stdin.readline())

for i in range(N):
    A, B = map(int, sys.stdin.readline()[:-1].split())
    print(int(A * B// gcd(A, B)))


