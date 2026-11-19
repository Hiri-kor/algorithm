def solution(arr):
    # answer = [[]]
    arr_len = len(arr)
    for a in arr:
        a_len = len(a)
        if a_len < arr_len:
            for i in range(arr_len - a_len):
                a.append(0)
    if a_len > arr_len:
        for i in range(a_len - arr_len):
            arr.append([0]*a_len)
    return arr