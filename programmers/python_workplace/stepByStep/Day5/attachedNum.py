#이어붙인 수 >>https://school.programmers.co.kr/learn/courses/30/lessons/181928
#solutioin
def solution(num_list):
    even, odd = '',''
    for i in num_list:
        if i%2: #i is odd
            odd += str(i)
        else: even += str(i)
    return int(even) + int (odd)

#testcase===================================
num_list = [5,7,8,3]
print(solution(num_list))
#===========================================

#answer1