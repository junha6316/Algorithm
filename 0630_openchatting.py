


def solution(records):
    name ={}
    answer=[]
    for record in reversed(records):
        li = record.split(" ")
        if len(li) ==2:
            state = li[0]
            id = li[1]
        else:
            state = li[0]
            id = li[1]
            nick = li[2]

        if id not in name.keys():
            name[id] = nick

        if state == "Change":
            name['id'] = nick
        elif state == "Enter":
            answer.append(f"{name[id]}님이 들어왔습니다.")
        elif state =="Leave":
            answer.append(f"{name[id]}님이 나갔습니다.")

    return answer[::-1]

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records))
'''
이름을 바꾸고 들어면 채팅방의 기록이 모두 바뀐 이름으로 기록된ㅏ.
나가지 않고 이름을 바꿔도 기록이 모두 바뀐 이름으로 기록된ㅏ
state id nickname
id : nickname
'''

def solution(records):
    name ={}
    answer=[]
    for record in records:
        li = record.split(" ")
        if len(li) == 2:
            state = li[0]
            id = li[1]
            nick=''
        else:
            state = li[0]
            id = li[1]
            nick = li[2]

            name[id] = nick
        if state !='Change':
            answer.append([id, state])


    for i in range(len(answer)):
        if answer[i][1] =='Enter':
            answer[i] = f"{name[answer[i][0]]}님이 들어왔습니다."
        elif answer[i][1] == 'Leave':
            answer[i] = f"{name[answer[i][0]]}님이 나갔습니다."
        else:
            pass
    return answer

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records))