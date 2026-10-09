def solution(myString, pat):
    answer = 0
    _str = myString.upper()
    _pat = pat.upper()
    if _pat in _str:
        answer = 1
    return answer