n, N = map(int, input().split())
num_li =[]
for i in range(n):
    num_li.append(int(input()))

start = 1
end = sum(num_li)
while(start <= end):
    l = (start + end+1) // 2
    c = sum([i//N for i in num_li])
    if N > c: #너무 크게 잘랐
        end = l - 1
    elif N <= c: #너무 작게 잘랐
        ans = l
        start = l + 1

print(ans)






