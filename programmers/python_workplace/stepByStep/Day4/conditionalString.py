#조건 문자열 >>https://school.programmers.co.kr/learn/challenges/training?order=acceptance_desc
#solution
def solution(ineq, eq, n, m):
    if eq == "!": eq = ""
    answer = int(eval(str(n) + ineq + eq + str(m)))
    return answer

#testcase=================================
ine, e, n_i, m_i = ">", "!", 20, 50
print(solution(ine, e, n_i, m_i))
#=========================================

#answer1
def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    return int(eval(f'{n} {ineq}{eq} {m}'))

#answer2
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))