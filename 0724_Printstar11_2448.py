N=int(input())
star =["  *  "," * * ","*****"]

def stars(star):
    result=[]
    N = len(star) #
    n = len(star)//3
    for i in range(0,N*2):
        if i // N ==0:
            result.append(" "*N+star[i]+" "*N)
        else:
            result.append(star[i % len(star)]+" "+star[i % len(star)])
    return result




while(len(star) < N):
    star =stars(star)

for i in star: print(i)

