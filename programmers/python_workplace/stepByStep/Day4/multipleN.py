#n의 배수 >>https://school.programmers.co.kr/learn/courses/30/lessons/181937
#solution
def solution(num, n):
    return (1 if(num%n == 0) else 0)

# #testcase===============================
# num_i, n_i = 34, 3
# print(solution(num_i, n_i))

# #======================================

#answer
def solution(num, n):
    return int(not(num % n))