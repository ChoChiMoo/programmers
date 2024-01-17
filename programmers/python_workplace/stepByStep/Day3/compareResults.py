#두 수의 연산값 비교하기 >>https://school.programmers.co.kr/learn/courses/30/lessons/181938
#solution
def solution(a, b):
    answer = int(max(int(str(a)+str(b)) , 2*a*b))
    return answer

#testcase=================================
ia, ib = 91, 2
print(solution(ia, ib))

#=========================================

#answer