def solution(myStr):
    for ch in "abc":
        myStr = myStr.replace(ch, " ")
    answer = myStr.split()
    return answer if answer else ["EMPTY"]