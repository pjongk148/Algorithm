import itertools
from collections import Counter

def solution(orders, course):
    from itertools import combinations
    from collections import Counter



    answer = []
    for i in course:
        temp = []
        for menu in orders:
            comb = combinations(sorted(menu), i)
            temp += comb
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) > 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    answer.sort()
    return answer