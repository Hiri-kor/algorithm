def solution(my_string):
    answer = [0] * 52
    for i in my_string:
        _ord = ord(i)
        if 65 <= _ord < 97:
            answer[_ord-65] += 1
        else:
            answer[_ord-71] += 1
    return answer