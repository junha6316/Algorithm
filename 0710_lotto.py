import sys

num_lis=[]

while(True):
    exm=list(map(int, sys.stdin.readline().split()))
    if exm == [0]:
        break
    else:
        num_lis.append(exm)

for num_li in num_lis:
    N = num_li.pop(0)
    for a in range(N):
        for b in range(a+1,N):
            for c in range(b+1,N):
                for d in range(c+1,N):
                    for e in range(d+1,N):
                        for f in range(e+1,N):
                            print(f'{num_li[a]} {num_li[b]} {num_li[c]} {num_li[d]} {num_li[e]} {num_li[f]}')
    print('')






