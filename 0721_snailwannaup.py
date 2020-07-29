def bs(A,B,n):
    answer = 0
    i=1
    while(answer != n):
        answer += A
        if answer == n: break
        answer -=B
        i+=1
    return i

A, B, N = map(int, input().split())
start = 1
end = 1000000000
result =-1
while(start <= end):
    mid = (start + end)//2
    distance = (A-B) *(mid-1) +A
    if (distance >= N):
        result = mid
        end = mid-1
    else:
        start = mid +1
print(result)





