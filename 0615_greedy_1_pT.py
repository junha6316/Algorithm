# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#     temp = [0b,0b,0b]
#
#     for i in range(1, n + 1):
#         if i not in lost:
#             temp[0] += '1'
#         else:
#             temp[0] += '0'
#
#     for i in range(1, n + 1):
#         if i in reserve:
#             temp[1] += '1'
#         else:
#             temp[1] += '0'
#
#     return

def solution(n, lost, reserve):
    answer = n - len(lost)
    for r_student in reserve:
        if r_student in lost:
            lost.remove(r_student)
            answer += 1

        elif r_student - 1 in lost:
            lost.remove(r_student - 1)
            answer += 1

        elif r_student + 1 in lost:
            lost.remove(r_student + 1)
            answer += 1

        #이전 시행에서 r_student가 reserve에 있었지만 r_student+1은 오늘 옷을 안가져왔지만 여분이 있는 친구 일수 있다.
    return answer

def solution(n, lost, reserve):
    losted = set(lost) - set(reserve)
    reserved = set(reserve) - set(lost)
    lost.sort()
    reserve.sort()
    answer =n-len(losted)

    for r_student in reserved:
        if r_student-1 in losted:
            losted.remove(r_student-1)
            answer +=1
        elif r_student+1 in losted:
            losted.remove(r_student+1)
            answer +=1
    return answer

n =5
lost =[2,4]
reserve =[1,3,5]

print(solution(n,lost,reserve))