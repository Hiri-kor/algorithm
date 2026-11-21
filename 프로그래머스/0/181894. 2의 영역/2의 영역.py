def solution(arr):
    if arr.count(2) == 0:
        return [-1]
    elif arr.count(2) == 1:
        return [2]
    else:
        first = arr.index(2)
        last = len(arr) - 1 - arr[::-1].index(2)
        return arr[first:last+1]