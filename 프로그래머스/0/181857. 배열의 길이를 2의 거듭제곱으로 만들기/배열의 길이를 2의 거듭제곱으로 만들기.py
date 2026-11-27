def solution(arr):
    _len = len(arr)
    num = 0
    while 2 ** num < _len:
        num += 1
    add_cnt = 2**num - _len
    if add_cnt == 0:
        return arr
    else:
        for i in range(add_cnt):
            arr.append(0)
        return arr