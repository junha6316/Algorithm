N= list(map(int, " ".join(input()).split()))
N.sort(reverse=True)

if N[-1] != 0:
    print(-1)
else:
    while(True):
        N.pop(-2)

        if len(N) >= 2:
            print(''.join(list(map(str, N))))
            break
        else:
            print(-1)
            break