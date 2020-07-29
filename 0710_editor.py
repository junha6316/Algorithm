import sys
word  =sys.stdin.readline()[:-1]
n_word = len(word)
c_index = len(word)
N= int(sys.stdin.readline())
cmds = [sys.stdin.readline()[:-1] for _ in range(N)]

for cmd in cmds:
    if cmd[0] =='P':
         word=word[0:c_index]+cmd[2]+word[c_index:]
         c_index +=1
         n_word +=1
    elif cmd == 'L':
        c_index -=1 if c_index != 0 else 0
    elif cmd == 'B':
        if c_index != 0:
            word= word[0:c_index-1]+word[c_index:]
            c_index -=1
            n_word -=1
        else:
            pass
    elif cmd == 'D':
        c_index += 1 if c_index != n_word-1 else 0

print(word)


