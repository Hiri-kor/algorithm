def solution(num_list):
    answer = 0
    _len = len(num_list)
    if _len > 10:
        for i in num_list:
            answer += i
    else:
        answer = 1
        for i in num_list:
            answer *= i
            
    return answer