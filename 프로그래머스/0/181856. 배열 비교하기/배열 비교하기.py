def solution(arr1, arr2):
    _len1 = len(arr1)
    _len2 = len(arr2)
    if _len1 > _len2:
        answer = 1
    if _len1 < _len2:
        answer = -1
    if _len1 == _len2:
        if sum(arr1) > sum(arr2):
            answer = 1
        elif sum(arr1) < sum(arr2):
            answer = -1
        else:
            answer = 0
    return answer