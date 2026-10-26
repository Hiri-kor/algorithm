def solution(my_string):
    answer = []
    ans = []
    for i in range(len(my_string)):
        ans.append(my_string[i:])
    answer = sorted(ans)
    return answer