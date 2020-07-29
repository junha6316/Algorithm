h =n//2
dx = [0,h,0,h ]
dy = [0,0,h,h]
for i in range(4):
    nx = x +dx[i]
    ny = y +dy[i]

    div(nx,ny,h)
    if 0<=nx<N and 0<=ny<N:

temp =[g[i][x:x+n] for i in range(y,y+n)]
def chck(temp):
    N= len(temp)
    if N==1: return True
    else:
        for i in range(N):
            for j in range(N):
                if temp[i][j] != temp[0][0]:
                    return False

    return True