def solution(str1, str2):
    answer = "".join(a + b for a, b in zip(str1, str2))    
    return answer