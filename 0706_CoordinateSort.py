import sys
N= int(sys.stdin.readline())
li=[list(map(int ,sys.stdin.readline().split())) for i in range(N)]

li= sorted(li, key = lambda x:x[1])
li = sorted(li, key = lambda x:x[0])

for i in li:
    print(f'{i[0]} i{1}')
