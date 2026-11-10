def solution(todo_list, finished):
    answer = []
    _len = len(finished)
    for i in range(_len):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer