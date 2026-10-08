def solution(arr, k):
    if k % 2 == 1:
        arr = [i * k for i in arr]
    else:
        arr = [i + k for i in arr]
    answer = arr
    return answer