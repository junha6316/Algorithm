import sys
def solution(cmd,result):
    if cmd[0:4] =="push":
        result.append(int(cmd[5:]))
    elif cmd =="pop":
        if len(result) ==0:
            print(-1)
        else:
            print(result.pop(0))
    elif cmd == "size":
        print(len(result))
    elif cmd == "empty":
        if len(result) ==0:
            print(1)
        else:
            print(0)
    elif cmd =="front":
        if len(result) != 0:
            print(result[0])
        else:
            print(-1)
    elif cmd =="back":
        if len(result) != 0:
            print(result[-1])
        else:
            print(-1)
    else:
        pass

    return result

N= int(sys.stdin.readline())
result=[]
for i in range(N):
    cmd=sys.stdin.readline()[:-1]

    if cmd[0:4] =="push": result.append(int(cmd[5:]))
    elif cmd =="pop":
        if len(result) ==0: print(-1)
        else: print(result.pop(0))
    elif cmd == "size": print(len(result))
    elif cmd == "empty":
        if len(result) ==0: print(1)
        else: print(0)
    elif cmd =="front":
        if len(result) != 0:print(result[0])
        else: print(-1)
    elif cmd =="back":
        if len(result) != 0: print(result[-1])
        else: print(-1)




