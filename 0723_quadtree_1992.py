N=int(input())
paper = [list(map(int, ' '.join(input()).split())) for i in range(N)]

def chk(temp):
    N= len(temp)
    if N ==1:
        return True
    for i in range(N):
        for j in range(N):
            if temp[i][j] != temp[0][0]:
                return False
    return True


def cut(tree,x,y,size):
    temp =[tree[i][x:x+size] for i in range(y,y+size)]
    check = chk(temp)
    half = size //2
    for i in temp: print(i)
    if check:
        return str(temp[0][0])

    else:
        dx = [0, half, 0, half]
        dy = [0, 0, half, half]
        zipp = '('
        for i in range(4):
            ux = x + dx[i]
            uy = y + dy[i]
            zipp += cut(tree, ux, uy, half)
        zipp +=')'


    return zipp



print(cut(paper,0,0,N))





