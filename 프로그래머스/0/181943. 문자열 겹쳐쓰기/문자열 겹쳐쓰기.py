def solution(my_string, overwrite_string, s):
    _len = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+_len:]
    return answer