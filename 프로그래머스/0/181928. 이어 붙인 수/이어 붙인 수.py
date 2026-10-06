def solution(num_list):
    N_2 = ''
    N_1 = ''
    for i in num_list:
        if i % 2 == 0:
            N_2 += str(i)
        else:
            N_1 += str(i)
    answer = int(N_1) + int(N_2)
    return answer