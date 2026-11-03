def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0 and code[i] == "1":
            mode = 1
            continue
        elif mode == 1 and code[i] == "1":
            mode = 0
            continue
        
        if mode == 0:
            if code[i] != 1 and i % 2 == 0:
                ret += code[i]
        if mode == 1:
            if code[i] != 1 and i % 2 == 1:
                ret += code[i]
                
    if ret == '':
        answer = "EMPTY"
    else:
        answer = ret
        
    return answer