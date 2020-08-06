s = input()
def operate(num1, num2, op):
    if op == '*':
        return num1*num2
    if op== '-':
        return num1-num2
    if op=='+':
        return num1+num2
idx=0

while(True):
    c=s[idx]
    if c =='-' and idx !=0:
        temp=''
        left = idx-1
        right = idx +1
        while(48 <= ord(s[left]) <= 57 and left >=0):
            temp += s[left]
            left -=1

        num1 = int(temp[::-1])
        temp=''

        while (48 <= ord(s[right]) <= 57 and right <= len(s)-1):
            temp += s[right]
            right +=1

        num2 = int(temp)

        result = operate(num1, num2, '-')

        s = s[:left+1] +str(result) + s[right:]

        print(s)
    else:
        idx+=1









