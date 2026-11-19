def solution(rank, attendance):
    lst = []
    for i in range(len(rank)):
        idx = rank.index(i + 1)
        if len(lst) >= 3:
            break
        if attendance[idx] == True:
            lst.append(idx)

    answer = 10000*lst[0] + 100*lst[1] + lst[2]
    
    return answer