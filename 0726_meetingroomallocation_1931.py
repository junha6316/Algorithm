# from collections import deque
#
# N= int(input())
# meet=[]
# for i in range(N):
#     st, end = map(int, input().split())
#     meet.append((st,end))
#
# meet_s =sorted(meet)
# meet_e = sorted(meet, key = lambda x:x[1])
# print(meet_s)
# print(meet_e)
# cnt =0
# sc=[]
# i=0
# while(i <= N-1):
#     if meet_s[i][1] < meet_e[i][1]:
#         end = meet_s[i][1]
#         sc.append(meet_s)
#     else:
#         end = meet_e[i][1]
#         sc.append(meet_e)
#
#     i+=1
#     cnt+=1
#
#
#     while(True):
#         if meet_s[i][1] <end:
#             i+=1
#             print(i)
#         else:
#             break
# print(sc)
#
#
# import sys
# def greedy(meeting):
#     cnt=0
#     start_time=0
#
#     for time in meeting:
#         if time[0]>= start_time:
#             start_time = time[1]
#             cnt +=1
#     return cnt
#
# if __name__ =="__main__":
#     N = int(input())
#     meet =[tuple(map(int, input().split())) for i in range(N)]
#     meet = sorted(meet, key = lambda x :x[0])
#     meet = sorted(meet, key = lambda x: x[1])
#     print(greedy(meet))
import sys
In =sys.stdin.readline

N = int(In())
meet =[(*map(int, In().split()),) for i in range(N)]
meet.sort()

cnt =0
start=float('inf')

for time in reversed(meet):
   if time[1] <= start:
       start = time[0]
       cnt +=1

print(cnt)
