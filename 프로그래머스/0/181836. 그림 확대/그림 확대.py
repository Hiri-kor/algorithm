def solution(picture, k):
    answer = []
    for pic in picture:
        _sum = ''
        for i in range(len(pic)):
            _sum += pic[i] * k
        for j in range(k):
            answer.append(_sum)
    return answer