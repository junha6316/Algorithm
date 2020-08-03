L, C= map(int, input().split())
charac = input().split()
charac.sort()

for i in range(0,C-L):
    q=[[0,charac[i]]]
    while(q):
        idx, c =q.pop(0)
        if len(c) == L:
            print(c)
        else:
            for j in range(idx+1,C):
                if charac[j] not in c:
                    q.append([j,c+charac[j]])

