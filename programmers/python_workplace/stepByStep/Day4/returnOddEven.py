#홀짝에 따라 다른 값 반환하기 >>https://school.programmers.co.kr/learn/courses/30/lessons/181935
#solution
def solution(n):
    answer = 0
    if(n%2):#if n<=even
        for i in range(1,n+1,2): #1,3,5{odd}
                answer += i
    else:
        for i in range(0,n+1,2): #0,2,4{even}
                answer += i**2
    return answer

#testcase========================================
n_i = 7
print(solution(n_i))
#================================================

#answer1
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])

#answer2
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)