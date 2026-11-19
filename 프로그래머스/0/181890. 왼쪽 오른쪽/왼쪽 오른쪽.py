def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []
    for i in range(len(str_list)):
        if str_list[i] == "l":
            answer = str_list[:i]
            break
        if str_list[i] == "r":
            answer = str_list[i+1:]
            break
        
    return answer