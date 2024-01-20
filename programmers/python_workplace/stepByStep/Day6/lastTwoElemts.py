#마지막 두 원소 >>https://school.programmers.co.kr/learn/courses/30/lessons/181927
#solution
def solution(list):
    list.append(list[-1] - list[-2] if num_list[-1] > num_list[-2] else list[-1] * 2)
    return list

#testcase=================================
num_list = [2, 1, 6]
print(solution(num_list))
#=========================================

#answer1
def solution(l):
    l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
    return l
