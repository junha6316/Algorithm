s = input()

N=len(s)
i= 1

# cnt=1
# answer =''
# start =s[0]
# s =s[1:]
# while(True):
#     if s.find(start) !=-1:
#         cnt+=1
#     else:
#         answer += str(cnt) +start
#         start = s[0]
#         cnt=1
#
#     s = s[1:]
#     if not s:
#         answer += str(cnt) +start
#         break
#
#
# print(answer)
# start =s[0:2]
# s =s[2:]
# cnt=1
# answer =''
# while(True):
#     if s.find(start) !=-1:
#         cnt+=1
#     else:
#         answer += str(cnt) +start
#         start = s[0:2]
#         cnt=1
#
#     s = s[2:]
#     if len(s)<=2:
#         if not s:
#             answer += str(cnt) +start
#         else:
#             answer += str(cnt) + start
#             answer += '1'+s
#         break
#
# print(answer)
def solution(s):
    N=len(s)
    Min =N
    for i in range(2,N//2):
        start =s[0:i]
        s =s[i:]
        cnt=1
        answer =''
        while(True):
            if s.find(start) !=-1:
                cnt+=1
            else:
                answer += str(cnt) +start
                start = s[0:i]
                cnt=1

            s = s[i:]
            if len(s)<=i:
                if not s:
                    answer += str(cnt) +start
                else:
                    answer += str(cnt) + start
                    answer += '1'+s
                break
            Min = min(answer,Min)
    return Min







