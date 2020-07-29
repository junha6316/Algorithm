from math import ceil, trunc
def solution(w, h):
    answer = w * h
    i = 0
    r = w / h
    temp=0
    if w>h:
        temp =w
        w=h
        h=temp

    while (True):
        temp += ceil(r*(i+1))-trunc(r*i)
        if(int((i+1) * r) == (i+1) * r):
            break
        i += 1

    return int(answer - temp *h/(i+1))

from math import gcd

def solution(w, h):
    answer = w * h
    temp=0
    GCD=gcd(w,h)
    if w>h:
        temp =w
        w=h
        h=temp
        temp=0

    r = w / h
    for i in range(GCD-1):
        if (int((i+1) * r) != (i+1) * r) and (int((i) * r) != (i) * r):
            temp += 2
        else:
            temp += 1

    return int(answer - temp * h / (i+1))







print(solution(8,12))
