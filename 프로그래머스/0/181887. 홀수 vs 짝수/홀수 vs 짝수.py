def solution(num_list):
    answer = 0
    fir_sum = 0
    sec_sum = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            fir_sum += num_list[i]
        else:
            sec_sum += num_list[i]
    if fir_sum > sec_sum:
        answer = fir_sum
    else:
        answer = sec_sum
    return answer