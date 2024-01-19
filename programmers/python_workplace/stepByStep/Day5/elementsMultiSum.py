#원소들의 곱과 합 >>https://school.programmers.co.kr/learn/courses/30/lessons/181929
#solution
def solution(num_list):
    multi, add = 1, 0
    for i in num_list:
        multi *= i
        add += i
    return int(not(multi > add**2))

#testcas==================================
num_list = [5, 7, 8, 3]
print(solution(num_list))
#=========================================

#answer1
def solution(num_list):
    mul = 1 
    for n in num_list:
        mul *= n
    return int(mul < sum(num_list) ** 2)