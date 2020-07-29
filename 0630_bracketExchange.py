import queue as q
def solution(st):
    qu=q.Queue()
    i=0
    n=len(st)
    while(i != n-1):
        for i in range(n):
            if st[i] == '(':
                qu.put('(')
            elif st[i] == ')' and qu.qsize() != 0:
                qu.get()

            if qu.qsize() ==0:
                u=st[:i+1]
                v=st[i:]
                break

        i += 1

    return u,v

st="(()())()"

print(solution(st))

# ''
#
#
# 1.check right bracket string
#
# '''
#
# def checkRightBracket(st):
#     qu=q.Queue()
#     for i in range(len(st)):
#         if st[i] == '(':
#             qu.put('(')
#         elif st[i] == ')' and qu.qsize() != 0:
#             qu.get()
#         elif st[i] ==')' and qu.qsize() ==0:
#             return False
#
#     if q.size() !=0:
#         return False
#     else:
#         return True

