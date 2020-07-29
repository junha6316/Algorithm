
s_loc, t_loc = map(int, input().split())
if s_loc == t_loc:
    print(0)
else:
    q =[s_loc]
    visit=[False for i in range(100001)]
    t=0
    isArrive= False
    while(True):
        q_temp=[]
        for i in range(len(q)):
            loc=q.pop()
            if loc ==t_loc:
                isArrive = True
                break
            else:
                if visit[loc] == False:
                    visit[loc] = True
                    if 0<=loc-1 and visit[loc-1] == False: q_temp.append(loc-1)
                    if 0<=loc+1 <=100000 and visit[loc+1] == False: q_temp.append(loc+1)
                    if 0<=2*loc <=100000 and visit[2*loc] == False : q_temp.append(2*loc)

        if isArrive:
            break
        else:
            q.extend(q_temp)
            t+=1

    print(t)








