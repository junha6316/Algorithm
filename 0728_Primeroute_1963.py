n= int(input())
N=10000
num = [False for i in range(10000)]
for i in range(2,100):
    if num[i] == False:
        for j in range(2*i,10000,i):
            num[j] = True

def findPrime(start):
    global num
    result=[]
    for i in range(10):
        for j in range(4):
            if int(start[j]) != i:
                if j == 0 and i==0:
                    pass
                else:
                    answer = start[:j] +str(i) +start[j+1:]
                    if num[int(answer)]== False:
                        result.append(answer)
    return result
for x in range(n):
    start, target = input().split()
    visit =[False for i in range(10000)]
    q=[start]
    move=0
    isTarget = False
    while(True):
        q_temp=[]
        for i in range(len(q)):
            start = q.pop(0)
            visit[int(start)] = True
            if start == target:
                isTarget =True
                break
            else:
                result = findPrime(start) #return Primelist
                for i in result:
                    if visit[int(i)] == False:
                        q_temp.append(i)
                    else:
                        pass
        if isTarget:
            break
        else:
            q.extend(q_temp)
            move+=1
    print(move)











