

N= int(input())
num_li = list(map(int, input().split()))
num_li.sort()

M= int(input())
ch_li = list(map(int, input().split()))

def bs(num):
    start = 0
    end = N-1
    while(start <= end):
        mid = (start+end)//2
        if num_li[mid] ==num:
            return 1
        elif num_li[mid] > num:
            end = mid -1
        else:
            start = mid +1
    return 0

result=[]
for num in ch_li:
    result.append(str(bs(num)))

print(' '.join(result))

