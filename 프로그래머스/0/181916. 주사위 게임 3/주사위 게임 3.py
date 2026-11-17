def solution(a, b, c, d):
    answer = 0
    numbers = [a, b, c, d]
    _set = set(numbers)
    if len(_set) == 1:
        answer = 1111 * a
    elif len(_set) == 2:
        p, q = _set
        if numbers.count(p) == 3:
            answer = (10 * p + q)**2
        elif numbers.count(p) == 1:
            answer = (10 * q + p)**2
        else:
            answer = (p + q) * abs(p-q)
    elif len(_set) == 3:
        p, q, r = _set
        if numbers.count(p) == 2:
            answer = q * r
        elif numbers.count(q) == 2:
            answer = p * r
        else:
            answer = p * q
    else:
        answer = min(numbers)
    return answer