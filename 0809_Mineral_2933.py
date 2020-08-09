R, C= map(int, input().split())

mineral = [' '.join(input()).split() for i in range(R)]

N= int(input())
throws = list(map(int, input().split()))

'''
던져서 없애는 함
DFS를 확인해서 마지막 높이가 0인게 있으면 True/False
떨어지게 만드는 함
'''
visited= [[False for i in range(C)] for i in range(R)]


def throw(h,n):
    if n % 2 ==0:
        for idx, c in enumerate(mineral[h]):
            if c =='x':
                mineral[h][idx] = '.'
                return idx
    if n % 2 == 1:
        for idx in range(C-1, -1, -1):
            if mineral[h][idx] =='x':
                mineral[h][idx] ='.'
                return idx
def move(mineral):


drow =[0,0,1,-1]
dcol =[1,-1,0,0]

def DFS(i, j):
    answer = False
    def rDFS(i,j):
        if i == R-1:
            nonlocal answer
            answer = True
            return

        for k in range(4):
            nrow = i + drow[k]
            ncol = j + dcol[k]
            if 0<=nrow<R and 0<=ncol<C and visited[nrow][ncol] ==False and mineral[nrow][ncol] =='x':
                visited[nrow][ncol] = True
                rDFS(nrow, ncol)
    rDFS(i,j)
    return answer

for idx, t in enumerate(throws):
    loc=throw(8-t, idx)
    print(DFS(8-t,loc+1))












