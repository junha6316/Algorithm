import sys

def solution(cmd,stack):
    if cmd[0:4] == "push":
        stack.append(int(cmd[5:]))
    elif cmd =="pop":
        if len(stack) ==0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd=="size":
        print(len(stack))

    elif cmd=="empty":
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif cmd =="top":
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[-1])

    return stack

N= int(sys.stdin.readline())
stack=[]
for i in range(N):
    cmd=sys.stdin.readline()[:-1]
    stack=solution(cmd,stack)
