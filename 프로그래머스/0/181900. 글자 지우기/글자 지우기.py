def solution(my_string, indices):
    answer = ''
    _len = len(my_string)
    lst = [0] * _len
    for i in indices:
        lst[i] = 1
    for i in range(_len):
        if lst[i] != 1:
            answer += my_string[i]
    
    return answer