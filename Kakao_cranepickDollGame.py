def solution(board, moves):
    M= len(board[0])
    N= len(board)
    answer =0
    exit=[]
    idx =[0 for i in range(M)]

    for i in range(M):
        for j in range(N):
            if board[j][i] !=0:
                idx[i]=j
                break

    while(moves):
        row = moves.pop(0)
        if idx[row-1] ==N:
            pass
        else:
            if len(exit) >0 and exit[-1] == board[idx[row-1]][row-1]:
                exit.pop()
                answer+=1
            else:
                exit.append(board[idx[row-1]][row-1])

            idx[row-1] +=1

    return answer

board=[[0,0,0,0,0],
       [0,0,1,0,3],
       [0,2,5,0,1],
       [4,2,4,4,2],
       [3,5,1,3,1]]
moves =[1,5,3,5,1,2,1,4]
print(solution(board, moves)*2)
