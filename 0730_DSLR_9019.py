

def D(A):
    A = 2* A
    if A > 9999:
        return A % 10000, 'D'
    else:
        return A, 'D'
def S(A):
    if A==0:
        return 9999, 'S'
    else:
        return A-1, 'S'
def L(A):
    A =str(A)
    A = A[1:] +A[0]
    return int(A), 'L'

def R(A):
    A= str(A)
    A = A[-1] +A[0:-1]
    return int(A), 'R'

from collections import deque
N= int(input())
for i in range(N):
    A, B =map(int, input().split())
    visited =[True]+[False for i in range(10000)]
    visited[A] = True
    queue= deque()
    queue.append((A,''))
    while(queue):
        val, path = queue.popleft()
        if val == B:
            ans=path
            break

        result, operator = D(val)
        if not visited[result]:
            visited[result] =True
            queue.append((result, path+operator))

        result, operator = S(val)
        if not visited[result]:
            visited[result] =True
            queue.append((result, path+operator))

        result, operator = L(val)
        if not visited[result]:
            visited[result] = True
            queue.append((result, path + operator))

        result, operator = R(val)
        if not visited[result]:
            visited[result] = True
            queue.append((result, path + operator))

    print(path)













