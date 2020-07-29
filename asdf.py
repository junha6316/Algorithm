import time

def bubble(arr):
    t =0
    N=len(arr)
    while(t<N-1):
        for i in range(N-1-t):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        t += 1
    return(arr)

def merge(arr):
    swap=0
    def div(arr):
        if len(arr) == 1: return arr
        mid = len(arr)//2
        left =arr[:mid]
        right = arr[mid:]

        left = div(left)
        right = div(right)

        return conquer(left, right)

    def conquer(left, right):
        result =[]

        while(len(left)>0 and len(right)>0):
            if left[0] > right[0]:
                result.append(right.pop(0))
                nonlocal swap
                swap +=1
            else:
                result.append(left.pop(0))

        if len(left)>0: result.extend(left)
        if len(right)>0: result.extend(right)

        return result
    div(arr)
    return swap

li = [i for i in reversed(range(100000))]

# start = time.time()
# bubble(li)
# print(f'bubble :{round(time.time()-start,2)}')

start = time.time()
print(merge(li))
print(f'merge: {round(time.time()-start,2)}')

1