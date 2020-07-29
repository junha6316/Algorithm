# dish = input()
# answer=10
# start=dish[0]
# for i in range(1,len(dish)):
#     if start != dish[i]:
#         answer +=10
#     else:
#         answer +=5
#
#     start = dish[i]
# print(answer)

# N=int(input())
# for i in range(N):
#     r, e, c = map(int, input().split())
#     if e-r > c : print("advertise")
#     elif e-r==c: print("does not matter")
#     elif c>e-r: print("do not advertise")

N=int(input())
def numberSum(serial):
    answer =0
    for i in serial:
        try:
            answer+= int(i)
        except:
            pass
    return answer

serial = [input() for i in range(N)]
serial = [(i, len(i), numberSum(i)) for i in serial]
serial=sorted(serial)
serial=sorted(serial, key=lambda x:x[2])
serial=sorted(serial, key=lambda x:x[1])
for i in serial: print(i)


