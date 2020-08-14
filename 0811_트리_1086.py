N= int(input()) #노드 개수
p =list(map(int, input().split()))
M= int(input())
dic={i :[] for i in range(N)}

for idx, pa in enumerate(p):
    if pa ==-1:
        pass
    else:
        dic[pa].append(idx)


q=[]
target = dic.pop(M)
q.append(target)

while(q):
    children = q.pop(0)
    for node in children:
        q.append(dic.pop(node))

answer=0

for node in dic:
    if len(dic[node]) ==0:
        answer +=1
print(answer)




