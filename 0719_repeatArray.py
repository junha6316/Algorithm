N, P= map(int, input().split())

tree={N:[]}
a=[N]
def newy(n, P):
    answer=0
    for i in str(n):
        temp=1
        for j in range(P):
            temp *= int(i)
        answer += temp
    return answer

st=N
while(True):
    num = newy(st,P)
    if num in a:
        break
    else:
        a.append(num)
    st=num


print(len(a[:a.index(num)]))




