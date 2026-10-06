def solution(num_str):
    answer = 0
    _len = len(num_str)
    for i in range(_len):
        answer += int(num_str[i])
    return answer