def MoveRight(key):
    N = len(key)
    M = len(key[0])
    for i in range(N):
        key[i]=('0 '+' '.join(map(str, key[i]))).split()[:-1]
    return key

def MoveLeft(key):
    N = len(key)
    M = len(key[0])
    for i in range(N):
        key[i] = (' '.join(map(str, key[i]))+' 0').split()[1:]
    return key

def MoveUp(key):
    M= len(key[0])
    zero =[0 for _ in range(M)]
    key.append(zero)
    return key[1:]

def MoveDown(key):
    M = len(key[0])
    zero = [0 for _ in range(M)]
    key =[zero]+ key
    return key[:-1]

def clockwise(key):
    N=len(key)
    result=[[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = key[j][N-1-i]
    return result
def nonclcokwise(key):
    N= len(key)
    result = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j 


key =[[0, 0, 0, 0],
      [1, 0, 0, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 0]]

key=  clockwise(key)
for i in key: print(i)
print('-'*10)
key=  clockwise(key)
for i in key: print(i)
print('-'*10)
key=  clockwise(key)
for i in key: print(i)
print('-'*10)
key=  clockwise(key)
for i in key: print(i)
print('-'*10)
key=  clockwise(key)
for i in key: print(i)
print('-'*10)

# key=  MoveRight(key)

