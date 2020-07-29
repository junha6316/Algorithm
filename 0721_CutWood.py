N, M = map(int, input().split())
woods =list(map(int, input().split()))


def cut(woods, H):
    answer =0
    for i in woods:
        if i >H:
            answer += i-H
    return answer

start=0
end = max(woods)
ans=0

while(start <= end):
    mid = (start + end)//2
    c = cut(woods, mid)
    if M==c:
        if cut(woods, mid+1) ==M:
            start = mid + 1
        else:
            break
    elif M > c:
        end = mid - 1
    else:
        ans =mid
        start = mid + 1

print(ans)



from collections import Counter

def get_how_long_to_get(trees, x):
    return sum((t-x)*c if t > x else 0 for t, c in trees.items())

def binary_search(lo, hi, pred):
    while lo <= hi:
        mid = (lo+hi)//2
        if pred(mid): hi=mid-1
        else:
            r=mid
            lo=mid+1
    return r

def get_maximum_height_of_saw(trees, M):
    def is_shorter_than_M(x):
        return get_how_long_to_get(trees, x) < M
    answer = binary_search(0, max(trees), is_shorter_than_M)
    return answer

_, M = map(int, input().split())
trees = Counter(map(int, input().split()))

print(get_maximum_height_of_saw(trees, M))