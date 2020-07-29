def solution(numbers, target):
     cnt = 0
     def operator(numbers, target, idx=0):
         if idx < len(numbers):
             numbers[idx] *= 1
             operator(numbers, target, idx+1)
             numbers[idx] *= -1
             operator(numbers, target, idx+1)

         elif sum(numbers) == target:
             nonlocal cnt
             cnt += 1

     operator(numbers, target)

     return cnt


print(operate([1,1]))




# numbers=[1,1,1,1,1]
# target= 5
#
# print(solution(numbers,target))
 #
 # while(True):
 #
 #        if target > fnode:
 #            fnode += numbers[i]
 #        elif target<fnode:
 #            fnode -= numbers[i]
 #        else:
 #             answer +=1
 #
 #        i+=1

def