
import sys
N= int(sys.stdin.readline())

answer =''
r=1
if N==0:
    print(0)
else:
    while(N!=0):
        if N> 0:
            r = N % 2
            N = -(N // 2)

        else:
            r = N % -2
            N = N // -2

            if r == -1:
                N = N + 1
                r = 1

        answer += str(r)

    print(answer[::-1])






