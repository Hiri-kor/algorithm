def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        _int = 1000001
        
        for i in arr[s:e+1]:
            if k < i < _int:
                _int = i
        
        if not _int == 1000001:
            answer.append(_int)
        else:
            answer.append(-1)
    
    return answer