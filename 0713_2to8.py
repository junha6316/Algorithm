# import sys
# B = sys.stdin.readline()[:-1]
# answer_r=''
# b=1
# a=1
# n=len(B)
# for i in range(n-1, -1, -3):
#     answer =0
#     for j in range(3):
#         answer += int(B[i-j])*b
#         b*=2
#     answer_r = answer_r+str(answer // a)
#     a *=8
#
# import sys
# B = sys.stdin.readline()[:-1]
# n=len(B)
# if n %3 == 1:
#     B = "00"+B
# elif n%3 == 2:
#     B= "0" +B
# answer_r=''
#
#
# for i in range(n-1, -1, -3):
#     answer = int(B[i])*1 + int(B[i-1])*2 + int(B[i-2])*4
#     answer_r += str(answer)
#
# print(answer_r[::-1])

def bins(N):
    i=4
    j=0
    answer =''
    N = int(N)
    while(j!=3):
        if N==0:
            answer += '0'
        else:
            a = N // i
        answer += str(a)
        i /= 2
        N = N % i
        j += 1

    return answer


# import sys
# N= sys.stdin.readline()[:-1]
# n= len(N)
# answer=''
#
# for i in reversed(range(n)):
#    answer = bins(N[i]) +answer
#    if len(answer) % 3 ==2 and i!=0:
#        answer = "0" +answer
#    elif len(answer) %3 ==1 and i!=0:
#        answer = "00" +answer
#
# print(answer)




print(bins('3'))