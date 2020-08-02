'''
09:00 부터 총 n회 t분 간경으로 역에 도착
하나의 셔틀에는 최대 m명의 승객이 탑승가능하다.

콘은 항상 마지막에 탑승
1번 운행 되면 무조건 09:00 전에 와야한다.
2번 운행되면 두번째 운행전에 와야한다.
'''

def changeTimetable(timetable):
    result=[]
    for schedule in timetable:
        result.append(list(map(int, schedule.split(':'))))

    result = sorted(result, key =lambda x:x[1])
    result = sorted(result, key = lambda x:x[0])

    return result

def ChangeStr(time):
    hour = str(time[0])
    min = str(time[1])
    if len(min) == 1:
        min ='0' + min

    if len(hour) == 1:
        hour ='0'+hour

    return f'{hour}:{min}'

print(ChangeStr([8,10]))

timetable =	['08:10', '08:01', '08:02', '08:03','08:03','08:03']
# print(changeTimetable(timetable))

def solution(n, t, m, timetable):
    timetable = changeTimetable(timetable)
    s =[[9,0]]
    for i in range(n-1):
        min = s[-1][1]+t
        hour = s[-1][0]
        if min >= 60:
            s.append([hour+1, min-60])
        else:
            s.append([hour, min])

    last =s[-1]
    for idx in range(len(timetable)-1, -1, -1):
        if timetable[idx][0] >last[0]:
            timetable.pop(idx)
        elif timetable[idx][0] == last[0] and timetable[idx][1] > last[1]:
            timetable.pop(idx)
        else:
            break

    while(len(timetable) !=0):
        time = s.pop(0)
        for i in range(m):
            if (time[0]>timetable[i][0] and time[1]>timetable[i][1]):



    return ChangeStr(s[-1])


print(solution(10,60,5,timetable))