


def solution(brown, yellow):
    for i in range(2,brown):
        h = i
        v = (brown +4 -2*i )//2
        if (h-2) *(v-2) == yellow and h>=v:
            return [h, v]

brown =10
yellow =2
'''
	1	
24	24
'''
print(solution(brown, yellow))