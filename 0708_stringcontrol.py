# import sys
# sent = ' '.join(sys.stdin.readline()[:-1]).split()
# dic={}
# abc='abcdefghijklmnopqrstuvwxyz'
# dic ={i : 0 for i in abc}
# for i in sent:
#     if i not in dic.keys():
#         dic[i] =1
#     else:
#         dic[i] += 1
# print(dic)
# answer =''
# for i in dic.values():
#     answer += str(i) +" "
# print(answer[:-1])
# import sys
# a=[0 for i in range(26)]
# s=sys.stdin.readline().strip()
# for i in s:a[ord(i)-ord('a')] +=
# for i in a:print(i,end=' ')

import sys
sent = ' '.join(sys.stdin.readline()[:-1]).split()
dic={}
abc='abcdefghijklmnopqrstuvwxyz'
dic ={i : -1 for i in abc}
for i in range(len(sent)):
    if dic[sent[i]] == -1:
        dic[sent[i]] =i
    else:
        pass

answer =''
for i in dic.values():
    answer += str(i) +" "
print(answer[:-1])
