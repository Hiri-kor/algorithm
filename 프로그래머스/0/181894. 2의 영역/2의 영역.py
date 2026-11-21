def solution(arr):
    reverse = arr[::-1]
    if arr.count(2) == 0:
        return [-1]
    elif arr.count(2) == 1:
        return [2]
    else:
        for i in arr:
            if i == 2:
                first = arr.index(i)
                break
        for j in reverse:
            if j == 2:
                last = len(arr) - 1 - reverse.index(j)
                break
        return arr[first:last+1]