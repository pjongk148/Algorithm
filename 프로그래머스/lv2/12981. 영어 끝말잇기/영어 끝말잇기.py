import math
def solution(n, words):
    count = 1;
    
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i] or len(words[i]) == 1: 
            if (i+1) % n ==0:
                return [n, (i+1)// n]
            else:
                return [(i+1) % n, math.ceil((i+1) / n)]
    return [0,0]