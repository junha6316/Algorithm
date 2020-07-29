# N= int(input())
# points =[list(map(int, input().split())) for _ in range(N)]
# points= sorted(points)

def div(points):
    if len(points) <= 3: return points
    mid = len(points) //2

    left = points[:mid]
    right = points[mid:]

    left = div(left)
    right= div(right)

    print(left, right)

    return

def cq(left, right):
    result =[]
    MIN=min(calcL(left), calcL(right))



def calcL(arr):
    result=[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            dx = arr[i][0] - arr[j][0]
            dy = arr[i][1] - arr[j][1]

            result.append(dx*dx + dy*dy)

    return min(result)

print(calcL([(1,2),(3,4),(4,5),(5,6)]))



