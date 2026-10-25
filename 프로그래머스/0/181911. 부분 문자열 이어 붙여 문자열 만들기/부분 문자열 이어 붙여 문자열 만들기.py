def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        x, y = parts[i]
        _str = my_strings[i]
        answer += _str[x : y+1]
    return answer