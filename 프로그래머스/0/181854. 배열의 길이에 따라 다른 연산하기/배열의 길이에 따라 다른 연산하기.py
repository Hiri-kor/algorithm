def solution(arr, n):
    answer = []
    _len = len(arr)
    if _len % 2 == 1:
        for i in range(0, _len, 2):
            arr[i] += n
    else:
        for i in range(1, _len, 2):
            arr[i] += n
    answer = arr
    return answer