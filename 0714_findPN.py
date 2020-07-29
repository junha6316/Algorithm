M, N = map(int, input().split())
M = M+1 if M ==1 else M

prime = [False]
i=0

for i in range(2, MAX+1)
    for idx, num in enumerate(num_li):
        if num % num_li[i] ==0 and num != num_li[i]:
            num_li.pop(idx)
    i+=1

for num in num_li:
    if num<M:
        pass
    else:
        print(num)


