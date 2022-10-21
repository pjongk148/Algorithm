def solution(board, moves):
    stack = []
    new_list = list(map(list, zip(*board)))
    cnt = 0
    for i in new_list:
        while (i[0] == 0):
            i.remove(0)
        
    for i in moves:
        if not new_list[i-1]:
            continue
        tmp = new_list[i-1].pop(0)
        if not stack:
            stack.append(tmp)
        else:
            if stack[-1] == tmp:
                stack.pop()
                cnt += 2
            else:
                stack.append(tmp)
    return cnt