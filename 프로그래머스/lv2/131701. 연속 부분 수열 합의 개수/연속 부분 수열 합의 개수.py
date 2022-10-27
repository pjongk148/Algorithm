def solution(elements):
    score = set()
    base = len(elements)
    elements *= 2
    for i in range(1,base+1):
        tmp = 0
        while tmp != base:
            score.add(sum(elements[tmp:tmp+i]))
            tmp += 1

    return len(score) 