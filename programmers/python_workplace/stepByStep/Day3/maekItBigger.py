#더 크게 합치기 >> https://school.programmers.co.kr/learn/courses/30/lessons/181939
#solution
def solution(a, b):
    sa = str(a)
    sb = str(b)
    answer = int((sa + sb) if(int(sa + sb) >= int(sb + sa)) else (sb + sa))
    return answer

# #testcase=================================
# ia, ib = input().strip().split(' ')
# print(solution(ia, ib))

# #=========================================

# #answer
# def solution(a, b):
#     return int(max(f"{a}{b}", f"{b}{a}"))