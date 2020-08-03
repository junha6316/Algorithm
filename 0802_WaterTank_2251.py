'''
8/3 7:18
'''
from collections import deque

tank = list(map(int, input().split()))
# A:tank[0] B=tank[1] C= tank[3]
q=deque([0,0,tank[2]])

que = q.popleft()
for i in range(0,3):
    for j in range(0,3):
        if i !=j:
            if que[i] !=0 and que[j] == 0:
                que[i] = tank[i] -tank[j]
                que[j] = tank[j]


a=[tank[0]-que[2], que[1], 0] if que[2]<= tank[1] else [tank[0], que[1], que[2]-tank[1]]












'''
1. 한 물통이 비거나
2. 다른 물통이 가득 찰때까지
한 물통이 비거나 다른 물통이 가득 찰때 까지 
구현하는 걸 못하겠음
[0,0,10]-[0,9,1]-[8, 1, 1]-[0, 1, 9]
         [8,0,2]-[8, 2, 0],[1, 9, 0]-[0,2,8]
1. 하나가 가득 차 있고 하나가 비어있음 부으면 된다.
2. 
'''




