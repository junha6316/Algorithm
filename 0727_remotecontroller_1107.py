import heapq as hq
n= int(input())
N = int(input())
num_li = list(map(int, input().split()))
channel=[]
for i in range(0,1000000+1):
    num = str(i)
    isBreak =True
    for c in num:
        if int(c) in num_li:
            isBreak =False

    if isBreak:
        hq.heappush(channel, abs(i-n))

print(min(abs(n-100),hq.heappop(channel)+len(str(n))))

