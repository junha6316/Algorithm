


def solution(people, limit):
    answer = 0
    idx = 0
    li=[]
    people.sort(reverse=True)
    while(len(people) !=0 ):
        li.append(people[idx])
        if limit > sum(li):
            if idx == len(people) - 1:
                answer += 1
                idx = 0
                for i in li:
                    people.remove(i)
                li = []
            else:
                idx += 1

        elif limit == sum(li):
            answer +=1
            for i in li:
                people.remove(i)
            li = []
            idx=0

        elif limit < sum(li):
            li.pop()
            if idx == len(people) - 1:
                answer += 1
                idx = 0
                for i in li:
                    people.remove(i)
                li = []
            else:
                idx += 1

    return answer

people=[70,80,50,50]
limit =100

#------------다른 사람 풀이-----------------

def solution(people, limit) :
    answer = 0
    people.sort()
    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

print(solution(people,limit))