def solution(n):
    answer = 0
    if n % 2 == 1:
        answer = n
        for i in range(1, n, 2):
            answer += i
    else:
        answer = n**2
        for j in range(0, n, 2):
            answer += j**2
    return answer