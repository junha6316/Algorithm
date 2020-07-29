import sys
N= int(sys.stdin.readline())
g=[list(map(int, ' '.join(sys.stdin.readline()).split())) for _ in range(N)]
n_r= len(g)
n_c = len(g[1])
visited=[[False for i in range(n_r)] for _ in range(n_c)]

def complex(g, visited,r,c):
    answer =0
    def DFS (g,visited, r_index=r, c_index=c ):
        if r_index < n_r and c_index< n_c and visited[r_index][c_index] == False:
            if g[r_index][c_index] == 1:
                nonlocal answer
                answer += 1
                visited[r_index][c_index] = True

            if  r_index < n_r-1 and g[r_index+1][c_index] ==1:
                DFS(g, visited, r_index + 1, c_index)
            if c_index < n_c-1 and g[r_index][c_index+1] == 1:
                DFS(g, visited, r_index, c_index + 1)
            if r_index >= 1 and g[r_index-1][c_index] == 1:
                DFS(g, visited, r_index - 1, c_index)
            if c_index >= 1 and g[r_index][c_index-1] == 1:
                DFS(g, visited, r_index, c_index - 1)

    DFS(g,visited)
    return visited, answer


li_answer=[]
for i in range(n_r):
    for j in range(n_c):
        if g[i][j] ==1 and visited[i][j]==False:
            visited, answer =complex(g,visited, i, j)
            li_answer.append(answer)

print(len(li_answer))
li_answer.sort()
for i in li_answer:
    print(i)

for gg,i in zip(visited,g) :
    print(i)
    print(gg)
'''
7
0110100
0111101
1110101
0100111
0100000
0111110
0111000
'''



