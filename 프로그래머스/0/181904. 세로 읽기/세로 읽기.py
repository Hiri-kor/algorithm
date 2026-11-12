def solution(my_string, m, c):
    answer = ''
    _len = len(my_string)
    for i in range(c-1, _len, m):
        answer += my_string[i]
    return answer