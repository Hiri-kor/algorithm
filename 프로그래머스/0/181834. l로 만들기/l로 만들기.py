def solution(myString):
    answer = ''
    _ord = ord("l")
    for k in myString:
        if ord(k) > _ord:
            answer += k
        else:
            answer += "l"
    return answer