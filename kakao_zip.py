def solution(msg):
    dic ={chr(64+i): i for i in range(1,27)}
    answer =[]
    idx=0
    last =26
    N=len(msg)
    w=msg[0]
    c=msg[1]
    while(idx<=N):
        for i in range(idx+1,len(msg)+1):
            if msg[idx:i] not in dic.keys():
                answer.append(dic[msg[idx:i-1]])
                last +=1
                dic[msg[idx:i]] = last
                break

        msg = msg[i-1:]
        print(msg)

        print(answer)


    return answer

print(solution('KAKAO'))






