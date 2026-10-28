def solution(date1, date2):
    answer = 0
    day1 = ''
    day2 = ''
    for i in range(3):
        day1 += str(date1[i])
        day2 += str(date2[i])
    x, y = int(day1), int(day2)
    if x < y:
        answer = 1
    return answer