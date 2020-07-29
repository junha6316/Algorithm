import sys
from operator import itemgetter



N=int(sys.stdin.readline())

arr=[int(sys.stdin.readline()) for i in range(N)]
dict={}

for i in range(N):
    if arr[i] not in dict.keys():
        dict[arr[i]] = 1
    else:
        dict[arr[i]]+= 1

dict = sorted(dict.items(), key=itemgetter(0))
dict = sorted(dict, key=itemgetter(1), reverse=True)
print(dict[0][0])




