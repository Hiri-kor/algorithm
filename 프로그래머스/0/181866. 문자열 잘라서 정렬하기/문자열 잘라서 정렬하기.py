def solution(myString):
    _lst = myString.split("x")
    answer = []
    for i in _lst:
        if i:
            answer.append(i)
    return sorted(answer)