def solution(m, n, puddles):
    mapp=[]
    if len(puddles) >0:
        puddles = sorted(puddles, key=lambda x: x[0])
        puddles= sorted(puddles, key = lambda x :x[1])

    for i in range(n):
        temp=[]
        for j in range(m):
            if i==0:
                temp.append(1)
            else:
                if j==0:
                    temp.append(1)
                else:
                    temp.append(0)
        mapp.append(temp)

    for i in range(len(mapp)): #
        for j in range(0,len(mapp[i])):
            if j==0:
                pass
            else:
                mapp[i][j] = mapp[i][j - 1] + mapp[i - 1][j]

            if len(puddles) > 0 and (j == puddles[0][0] - 1) and (i == puddles[0][1] - 1):
                mapp[puddles[0][1] - 1][puddles[0][0] - 1] = 0
                puddles.pop(0)

    return mapp

m=5
n=5
puddles=[]
print(solution(m,n,puddles))



