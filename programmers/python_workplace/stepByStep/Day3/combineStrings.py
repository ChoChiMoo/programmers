#문자열 섞기 >>https://school.programmers.co.kr/learn/courses/30/lessons/181942
#solution


def solution(str1, str2):
    answer = ''
    for i in range(0, len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer

stra, strb = map(str, input().strip().split(' '))

print(solution(stra, strb))

#answer