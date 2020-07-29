import sys
def solution(st):
    stack=[]
    for i in st:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                return "NO"
            else:
                stack.pop()

    if len(stack) != 0:
        return "NO"

    return "YES"


N = int(sys.stdin.readline())
for i in range(N):
    print(solution(sys.stdin.readline()[:-1]))
