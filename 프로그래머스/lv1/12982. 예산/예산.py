def solution(d, budget):
    d.sort()
    total = 0
    cnt = 0 
    for i in d:
        total += i
        if total <= budget:
            cnt += 1
    
    return cnt