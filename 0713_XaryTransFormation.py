import sys
#N, B = map(int, sys.stdin.readline()[:-1].split())

# dic ={i:chr(i+55) for i in range(10,36)}
# answer =''
# while(N!=0):
#     R = N % B
#     N = N // B
#
#     if R >= 10:
#         answer += dic[R]
#     else:
#         answer += str(R)
#
#
# print(answer[::-1])

N, B = sys.stdin.readline()[:-1].split()
B= int(B)

dic ={chr(i+55):i for i in range(10,36)}
answer=0
i=1
for c in reversed(range(len(N))):
    try:
        answer += int(N[c]) * i
    except:
        answer += dic[N[c]] * i

    i *= B

print(answer)

