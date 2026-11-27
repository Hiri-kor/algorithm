def solution(strArr):
    map = [0] * 31
    for i in strArr:
        map[len(i)] += 1
    answer = max(map)
    return answer