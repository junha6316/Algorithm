

# def fac(N):
#     answer=1
#     while(N>1):
#         answer *= N
#         N -=1
#     return answer
N=int(input())
answer =0
for i in range(1,N+1):
    if i % 5 ==0 and  i>=5:
        while(i % 5 ==0):
            i = i//5
            answer +=1

print(answer)



