#등차수열의 특정한 항만 더하기 >>https://school.programmers.co.kr/learn/courses/30/lessons/181931
#solution
def solution(a, d, included):
    sum = 0
    for i in range(len(included)):
        if(included[i]): sum += a + d * i
    return sum

#testcase==============================
a,d = 3,4
included = [1,0,0,1,1]
print(solution(a,d,included))

#======================================

#answer1
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer