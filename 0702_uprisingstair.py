N= int(input())

if N==1:
    print(10)
else:
    li=[1 for i in range(10)]
    for i in range(1,N):
        for i in range(10):
            li[i] = sum(li[i:])

    print(li)
    print(sum(li))