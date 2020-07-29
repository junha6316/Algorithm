import sys
A , B = map(int, sys.stdin.readline().split())
N= int(sys.stdin.readline())
num_li=list(sys.stdin.readline().split())

def trans(N, A, B):
    dec=0
    i=1
    answer=''
    for idx in reversed(range(len(N))):
        dec += int(N[idx])*i
        i*=A

    while(dec !=0):
        r= dec % B
        dec = dec // B
        answer += str(r)
    return answer

answer = trans(num_li, A, B)[::-1]
print(' '.join(answer))