N,C = map(int, input().split())
num_li =[]
for i in range(N):
    num_li.append(int(input()))

num_li.sort()
start = 1
end = num_li[-1]-num_li[0]

def imp(num_li,l):
    answer=1
    st = 0
    end = 1
    while(end<len(num_li)-1):
        if  num_li[end] - num_li[st] >=l:
            answer +=1
            st =end
            end +=1
        else:
            end +=1

    return answer

while(start <= end):
    mid = (start+end)//2
    nl = imp(num_li,mid)
    if C <= nl:
        start = mid + 1
        ans =mid

    else:
        end = mid-1


print(ans)