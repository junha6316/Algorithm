import heapq as hq
import sys
N= int(sys.stdin.readline())
heap1 =[] #최대 힙
heap2 =[] #최소


for i in range(1,N+1):
    n = int(sys.stdin.readline())
    if i == 1:
        mid = n
    else:
        if mid >=n:
            hq.heappush(heap1,(-n,n))
        else:
            hq.heappush(heap2,n)

        if abs(len(heap1)-len(heap2)) <=1 :
            pass

        elif len(heap1) < len(heap2):
            hq.heappush(heap1,mid)
            mid = hq.heappop(heap1)[1]

        elif len(heap1) > len(heap2):
            hq.heappush(heap2, mid)
            mid = hq.heappop(heap2)



    print(mid)







