def solution(arr):
    answer = 1
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if not arr[i][j] == arr[j][i]:
                answer = 0
    return answer