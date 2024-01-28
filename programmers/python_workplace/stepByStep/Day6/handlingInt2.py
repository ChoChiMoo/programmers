#수 조작하기 2 >>https://school.programmers.co.kr/learn/courses/30/lessons/181925
#solution
def solution(numLog):
    answer = []
    for i in range(len(numLog)-1):
        keyvalue = numLog[i + 1] - numLog[i]
        key = { 1:'w', -1:'s', 10:'d', -10:'a'}
        answer.append(key[keyvalue])
    return ''.join(answer)

#testcase=====================================
numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(solution(numLog))
#=============================================

#answer