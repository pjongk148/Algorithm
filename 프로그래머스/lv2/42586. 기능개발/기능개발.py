import math 
def solution(progresses, speeds):
    from collections import Counter

    count =[]
    for _ in range(len(progresses)):
        count.append(math.ceil((100 - progresses[_])/speeds[_]))

    for _ in range(1,len(count)):
        if count[_] < count[_-1]:
            count[_] = count[_-1]


    answer = list(Counter(count).values())
    return answer