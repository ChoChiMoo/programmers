#수 조작하기 1 >>https://school.programmers.co.kr/learn/courses/30/lessons/181926
#solution
def solution(n, control):
    for i in list(control):
        if i == "w": n += 1
        elif i == "s": n -= 1
        elif i == "d": n += 10
        elif i == "a": n -= 10
    return n

#testcase====================================
control = 'wsdawsdassw'
n = 0
print(solution(n, control))

#============================================

#answer1
def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer

#answer2
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])