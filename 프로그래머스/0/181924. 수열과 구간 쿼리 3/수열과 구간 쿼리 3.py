def solution(arr, queries):
    for x, y in queries:
        arr[x], arr[y] = arr[y], arr[x]
    answer = arr
    return answer