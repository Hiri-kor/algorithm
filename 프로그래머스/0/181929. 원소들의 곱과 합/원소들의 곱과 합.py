def solution(num_list):
    A = 1
    B = 0
    for i in num_list:
        A *= i
        B += i
    if A < B**2:
        answer = 1
    else:
        answer = 0
    return answer