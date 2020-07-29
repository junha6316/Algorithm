N=int(input())

paper =[list(map(int, input().split())) for i in range(N)]

def chk(temp,N):
    fnum=temp[0][0]
    if N == 1:
        return True
    else:
        for i in range(N):
            for j in range(N):
                if temp[i][j] != fnum:
                    return False
    return True

result={-1:0, 1:0 ,0:0}

def cut(paper, x, y, size,result):
    temp_paper =[row[x:x+size] for row in paper[y:y+size]]
    check = chk(temp_paper, size)

    third = size //3
    if check:
        kind = temp_paper[0][0]
        if size == len(paper):
            result[kind] += 1
            return

        return temp_paper[0][0]

    else:
        for i in range(3):
            for j in range(3):
                nx= x + i * third
                ny =y + j * third
                kind= cut(paper, nx, ny, third,result)

        if kind == -1: result[-1] += 1
        elif kind == 1: result[1] += 1
        elif kind == 0: result[0] += 1




cut(paper, 0,0, N, result)
for i,values in result.items(): print(values)


