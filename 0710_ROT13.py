import sys
word = sys.stdin.readline()[:-1]

answer=''
for idx, c in enumerate(word):
    num = ord(c)
    if 65 <= num <= 90 :
        answer += chr((num+13) % 89 + ((num+13)//90)*64)
    elif 97 <= num <= 122:
        answer += chr((num + 13)% 122 + ((num+13)//122)*96)
    elif num==32:
        answer += ' '
    elif 48 <= num <=57:
        answer += c

print(answer)


