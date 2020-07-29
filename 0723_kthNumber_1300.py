N= int(input())
k= int(input())

low =0
high =k # k번째 수는 k를 넘을 수 없다.
answer= 0

while(low<=high):
    mid = (low+high)//2
    count =0
    for i in range(1, N+1):
        count = count + min(mid//i,N)

    if count <k:
        low = mid+1
    else:
        answer =mid
        high =mid -1
print(answer)