#공배수 >> https://school.programmers.co.kr/learn/courses/30/lessons/181936
#solution
def solution(number, n, m):
    return int(not(number%n or number%m))


#testcase=======================================
number_i, n_i, m_i = 60, 2, 3
print(solution(number_i, n_i, m_i))

#===============================================

#answer