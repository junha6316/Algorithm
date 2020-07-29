N=int(input())
pos=[]
neg=[]
zero_cnt =0
one_cnt=0
answer =0
for i in range(N):
    num = int(input())
    if num>0:
        pos.append(num)
        if num ==1:
            one_cnt +=1
    else:
        neg.append(num)
        if num ==0:
            zero_cnt +=1

neg.sort()
if zero_cnt >1:
    for i in range(zero_cnt-1):neg.pop()

pos.sort()
if one_cnt >1:
    for i in range(one_cnt-1):
        answer+= pos.pop(0)
n_ne = len(neg)
n_pos= len(pos)

if n_ne !=0:
    if n_ne % 2 ==0 and neg[-1] !=0:
        for i in range(0,n_ne,2): answer += neg[i] * neg[i + 1]
    elif n_ne % 2 ==0 and neg[-1] ==0:
        for i in range(0,n_ne-2,2): answer += neg[i] * neg[i + 1]

    elif n_ne % 2 !=0 and neg[-1]==0:
        for i in range(0,n_ne-1,2): answer += neg[i] * neg[i + 1]

    elif n_ne % 2 != 0 and neg[-1] !=0:
        answer += neg[-1]
        for i in range(0,n_ne-1,2): answer += neg[i] * neg[i + 1]

if n_pos !=0:
    if n_pos %2 ==0 and pos[0] ==1:
        answer += pos[0] +pos[1]
        for i in range(2,n_pos,2):
            answer += pos[i] * pos[i+1]

    elif n_pos %2 ==0 and pos[0] !=1:
        for i in range(0, n_pos, 2):
            answer += pos[i] * pos[i + 1]

    elif n_pos %2 !=0 and pos[0] == 1:
        answer += pos[0]
        for i in range(1, n_pos, 2):
            answer += pos[i] * pos[i + 1]

    elif n_pos % 2 != 0 and pos[0] != 1:
        answer += pos[0]
        for i in range(1,n_pos,2):
            answer += pos[i] * pos[i + 1]

print(answer)









