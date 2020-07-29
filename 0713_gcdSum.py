import sys

N= int(sys.stdin.readline())
def gcd(A,B):
    while(B !=0):
        r= A%B
        A= B
        B= r
    return A

for i in range(N):
    gcd_li=[]
    num_li=list(map(int, sys.stdin.readline().split()))
    subN=num_li.pop(0)

    for i in range(subN):
        for j in range(i+1, subN):
           gcd_li.append(gcd(num_li[i], num_li[j]))


    print(sum(list(gcd_li)))
