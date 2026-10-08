def solution(myString, pat):
    answer = 0
    _str = myString.translate(str.maketrans({"A":"B", "B":"A"}))
    if pat in _str:
        answer = 1
    return answer