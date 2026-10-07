def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)):
        if is_suffix == my_string[i:]:
            answer = 1
            break
    return answer