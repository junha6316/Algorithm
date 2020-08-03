N= int(input())

recs=[list(map(int, input().split())) for i in range(N)]
visited =[False for i in range(N)]
answer=0
while(False in visited):
    for i in range(N):
        if not visited[i]:
            q = [recs[i]]
            visited[i]=True
            print(123)
            while q:
                print(q)
                x1, y1, x2, y2 = q.pop(0)
                for idx in range(len(recs)):
                    if visited[idx] == False:
                        X1, Y1, X2, Y2 = recs[idx]
                        if x1<X2<x2 and y1<Y2<y2 and x1<X1<x2 and y1<Y1<y2:
                            pass
                        elif (x1<=X2<=x2 and y1<=Y2<=y2) or (x1<=X1<=x2 and y1<=Y1<=y2):
                            visited[idx] =True
                            q.append(recs[idx])

                        elif (x1<=X2<=x2 and y1<=Y1<=y2) or (x1<=X1<=x2 and y1<=Y2<=y2):
                            visited[idx] = True
                            q.append(recs[idx])

            answer += 1

print(answer)



