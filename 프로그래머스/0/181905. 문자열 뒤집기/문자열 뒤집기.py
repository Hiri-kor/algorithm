def solution(my_string, s, e):
    answer = ''
    s_e = ''
    for i in range(s):
        answer += my_string[i]
    for j in range(s, e+1):
        s_e += my_string[j]
    answer += s_e[::-1]
    for l in range(e+1, len(my_string)):
        answer += my_string[l]
    
    return answer