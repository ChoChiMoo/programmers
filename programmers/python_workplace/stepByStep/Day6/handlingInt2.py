#수 조작하기 2 >>https://school.programmers.co.kr/learn/courses/30/lessons/181925
#solution
def solution(numLog):
    answer = ''
    key = { 1:'w', -1:'s', 10:'d', -10:'a'}
    for i in range(len(numLog)-1):
        answer.append(key[numLog[i + 1] - numLog[i]])
    return answer

#testcase=====================================
numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(solution(numLog))
#=============================================

#answer1
def solution(numLog):
    answer = ''
    key = { 1:'w', -1:'s', 10:'d', -10:'a'}
    for i in range(len(numLog)-1):
        answer += key[numLog[i + 1] - numLog[i]]
    return answer
