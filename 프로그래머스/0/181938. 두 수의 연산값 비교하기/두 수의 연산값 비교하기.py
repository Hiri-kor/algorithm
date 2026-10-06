def solution(a, b):
    i = int(str(a)+str(b))
    j = 2*a*b
    if i >= j:
        answer = i
    else:
        answer = j
    return answer