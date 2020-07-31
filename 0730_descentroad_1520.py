N, M = map(int, input().split())
m = [list(map(int, input().split())) for i in range(N)]
dp =[[0 for i in range(M+1)] for i in range(N+1)]
answer =0
dx=[1,0]
dy=[0,1]
q=[[1,1]]

for i in range(1,)

def dfs():
    ans =0
    def rdfs(i,j):
        if i==N-1 and j ==M-1:
            nonlocal ans
            ans +=1
            return

        else:
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<M:
                    if m[i][j]>m[nx][ny]:
                        rdfs(nx,ny)

    rdfs(1,1)

    return ans
#
# print(dfs())












