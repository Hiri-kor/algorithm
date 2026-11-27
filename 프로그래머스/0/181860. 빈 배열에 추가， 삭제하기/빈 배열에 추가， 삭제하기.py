def solution(arr, flag):
    answer = []
    _len = len(flag)
    for i in range(_len):
        if flag[i]:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer