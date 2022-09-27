def solution(brown, yellow):
    x = 1
    while ((x+2)*(yellow/x +2) != yellow+brown):
        x += 1
        
    if x >= yellow/x:
        return [x+2,yellow/x+2]
    return [yellow/x+2,x+2]