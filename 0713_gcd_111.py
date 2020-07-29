import sys
A, B=map(int, sys.stdin.readline())

def gcd(A,B):
    while(B!=0):
        r = A%B
        A= B
        B=r
    return A

print(gcd(A,B)*'1')