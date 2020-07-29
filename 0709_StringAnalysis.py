import sys
answer_li=[]
for i in range(2):
    while(sys.stdin.readline()[:-1]!= 0):

        sentence = sys.stdin.readline().split()[:-1]
        print(sentence)
        answer = [0, 0, 0, 0]
        for c in sentence:
            if ord(c) >= 97 and ord(c) <= 122:
                answer[0] += 1
            elif ord(c) >= 65 and ord(c) <= 90:
                answer[1] +=1
            elif ord(c) >=48 and ord(c) <= 57:
                answer[2] += 1
            elif ord(c) ==32:
                answer[3] += 1
        for i in range(len(answer)):
            answer[i] = str(answer)

        answer_li.append(answer)

for answer in answer_li:
    print(' '.join(answer))





