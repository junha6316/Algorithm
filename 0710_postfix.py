import sys
w=sys.stdin.readline()[:-1]
post =[]

for i in range(len(w)):
    post.append(w[i:])

post.sort()

for i in post:
    print(i)
