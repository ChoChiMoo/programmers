def solution(my_string, overwrite_string, s):
    answer = str(my_string[0:s] + overwrite_string + my_string[len(overwrite_string):])
    return answer

my_string_i, overwrite_string_i, s_i = map(str, input().strip().split(' '))
s = int(s_i)

strings = list(my_string_i)
overwrite = list(overwrite_string_i)

print(solution(strings, overwrite, s))