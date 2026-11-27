def solution(myString):
    answer = []
    _split = myString.split("x")
    for i in _split:
        answer.append(len(i))
    return answer