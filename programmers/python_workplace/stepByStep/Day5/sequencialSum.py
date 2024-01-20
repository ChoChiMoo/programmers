#등차수열의 특정한 항만 더하기 >>https://school.programmers.co.kr/learn/courses/30/lessons/181931
#solution
def solution(a, d, included):
    sum = 0
    for i in range(1,len(included)):
        if(included[i-1]):
            sum += a+(d*(i-1))
    return sum

#testcase==============================
a,d = 3,4
included = [1,0,0,1,1]
print(solution(a,d,included))

#======================================

#answer1