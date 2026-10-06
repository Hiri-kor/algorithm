def solution(a, b):
    answer = 0
    str_a = str(a)
    str_b = str(b)
    a_b = int(str_a + str_b)
    b_a = int(str_b + str_a)
    if a_b >= b_a:
        answer = a_b
    else:
        answer = b_a
    return answer