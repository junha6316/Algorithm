
def calcMin(start,end):
    start = list(map(int, start.split(':')))
    end = list(map(int, end.split(':')))
    if start[1] <= end[1]:
        return (end[0]-start[0])*60 + end[1] -start[1]
    else:
        return(end[0]-1-start[0])*60 + end[1]+60-start[1]

def transform(m):
    note = ['C#', 'D#', 'F#', 'A#', 'G#', 'C', 'D', 'E', 'F', 'G', 'A', 'B']
    note_dic = {note[i]: chr(65 + i) for i in range(12)}
    result=''
    for idx, note in enumerate(m):
        if m[idx] == '#': pass
        elif idx < len(m)-1 and m[idx+1] == '#':
            result += note_dic[m[idx:idx+2]]
        else:
            result += note_dic[m[idx]]

    return result

def solution(m, musicinfos):
    m = transform(m)
    answer=[]
    for music_info in musicinfos:
        song = ''
        start, end, name, cord = music_info.split(',')
        cord = transform(cord)
        dur = calcMin(start, end)

        for i in range(dur):
            song += cord[i % len(cord)]

        if song.find(m) != -1:
            answer.append(name)
        else:
            pass
    answer = sorted(answer, key=len, reverse=True)
    return answer



m='AB'
musicinfos =["12:00,12:14,' ',ABCDEFG", "13:00,13:05,WORLD,ABCDEF"]
musicinfos =[]
print(solution(m, musicinfos))


print(calcMin('00:30','1:29'))
print(transform('C#DE'))