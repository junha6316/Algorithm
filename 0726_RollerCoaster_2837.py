R, C = map(int, input().split())

mapp = [list(map(int, input().split())) for i in range(R)]
answer =''
if R % 2 !=0:
    for i in range(C):
        if i % 2 == 0:
            answer += 'D'*(R-1)
        else:
            answer += 'U'*(R-1)
        answer += 'R'

elif R % 2 == 0:
    for i in range(R):
        if i %2 ==0:
            answer +='R'*(C-1)
        else:
            answer +='L'*(C-1)
        answer+='D'

print(answer[:-1])


