from collections import Counter
N= int(input())
num_li = list(map(int, input().split()))
num_li = Counter(num_li)

M= int(input())
ch_li = list(map(int, input().split()))

result=[]
for num in ch_li:
    try:
        result.append(str(num_li[num]))
    except:
        result.append(str(0))

print(' '.join(result))
