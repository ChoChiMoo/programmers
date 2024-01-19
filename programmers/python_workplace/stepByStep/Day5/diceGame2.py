#주사위 게임 2 >>https://school.programmers.co.kr/learn/courses/30/lessons/181930
#solution
def solution(a, b, c):
    answer = 0
    if a == b and a == c: #all same
        answer = ((3*a) * (3*a**2) * (3*a**3))
    elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b): #one different
        answer = ((a + b + c) * (a**2 + b**2 + c**2))
    else:
        answer = (a + b + c)
    return answer

#testcase===================================
ai, bi, ci = 4, 4, 4
print(solution(ai, bi, ci))
#===========================================

#answer1
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)