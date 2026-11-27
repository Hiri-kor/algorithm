def solution(num_list):
    answer = 0
    for i in num_list:
        cnt = 0
        while i > 1:
            if i % 2 == 0:
                i = i // 2
                cnt += 1
            else:
                i = (i-1) // 2
                cnt += 1
        answer += cnt
    return answer