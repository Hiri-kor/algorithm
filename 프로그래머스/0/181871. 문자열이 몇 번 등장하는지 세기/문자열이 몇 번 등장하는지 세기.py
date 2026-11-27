def solution(myString, pat):
    answer = 0
    _len = len(pat)
    for i in range(len(myString)-_len+1):
        if myString[i:i+_len] == pat:
            answer += 1
    return answer