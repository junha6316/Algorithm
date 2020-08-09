import heapq as hq
root=[i for i in range(1,8)]
root=[3,9,20,'null','null',15,7]
n= len(root)+1

parents=[(0,0,0)]
result=[(root[0],0,0)]


while parents:
    p, X_p, Y_p = parents.pop(0)
    if 2*p+2 < len(root):

        result.append((root[2*p+1], X_p+1, Y_p-1))
        result.append((root[2*p+2], X_p-1, Y_p-1))


        parents.append((2 * p + 1, X_p + 1, Y_p - 1))
        parents.append((2 * p + 2, X_p - 1, Y_p - 1))


result =sorted(result, key =lambda x:x[2], reverse=True)
result =sorted(result, key = lambda x:x[1], reverse=True)

answer =[]
temp=[]
for idx, re in enumerate(result):
    if result == null
    if idx != len(result)-1 and result[idx][1] == result[idx+1][1]:
        temp.append(re[0])
    else:
        temp.append(re[0])
        answer.append(temp)
        temp=[]
print(answer)







