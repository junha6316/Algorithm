import sys
N= int(sys.stdin.readline())

result =[]

for i in range(N):
    n = len(result)
    cmd = sys.stdin.readline()[:-1]
    temp=[]
    if cmd[0:10] == "push_front":
        result = [int(cmd[11:])]+result
    elif cmd[0:9] == "push_back":
        result.append(int(cmd[10:]))
    elif cmd =="pop_front":
        if n ==0:
            print(-1)
        else:
            print(result.pop(0))
    elif cmd =="pop_back":
        if n == 0:
            print(-1)
        else:
            print(result.pop())
    elif cmd=="size":
        print(n)
    elif cmd=="empty":
        if n ==0:
            print(1)
        else:
            print(0)
    elif cmd =="front":
        if n ==0:
            print(-1)
        else:
            print(result[0])
    elif cmd =="back":
        if n ==0:
            print(-1)
        else:
            print(result[-1])

