'''
속한 열과 네모를 확인함면 된다.
'''
from collections import Counter
game = [list(map(int, input().split())) for i in range(9)]
count =[i for i in range(1, 10)]
count = Counter(count)
print((count-Counter(game[0])))
def lineOne(game,i,j):
    cnt =0
    for k in game[i]:
        if k == 0:
            cnt+=1
    if cnt == 1:
        return True


for i in range(9):
    for j in range(9):
        if game[i][j] == 0 and lineOne(game,i,j):
            break

