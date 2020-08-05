
def findchild(begin, words):
    result=[]
    N= len(begin)
    for word in words:
        cnt = 0
        for i in range(N):
            if begin[i] == word[i]:
                cnt+=1
        if cnt == N -1:
            result.append(word)
    return result
def solution(begin, target, words):
    answer =0
    visited= [False for i in range(len(words))]
    words =[(words[idx], idx) for idx in range(len(words))]
    def dfs(begin, depth):
        if begin ==target:
            return depth




    if target not in words:
        return 0


def solution(begin, target, words):
    if target not in words:
        return 0
    visited=[]
    q=[]
    depth=0
    q.append((begin,depth))

    while q:
        begin, depth=q.pop()
        if begin == target:
            return depth

        for word in findchild(begin, words):
            if word not in visited:
                visited.append(word)
                q.append((word, depth+1))
    return 0





begin ="hit"
words=['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print(solution(begin,'cog',words))


