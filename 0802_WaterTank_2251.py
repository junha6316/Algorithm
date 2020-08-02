from collections import deque

tank = list(map(int, input().split()))
# A:tank[0] B=tank[1] C= tank[3]
q=deque([0,0,C])

for i in range(0,3):
    for j in range(i+1,3):
        if tank[i] == q:



'''
1. 한 물통이 비거나
2. 다른 물통이 가득 찰때까지
한 물통이 비거나 다른 물통이 가득 찰때 까지 
구현하는 걸 못하겠음
[0,0,1
[0,9,1]
[8,0,2]
'''




