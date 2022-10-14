import itertools
from collections import Counter
def solution(orders, course):
    
    arr = []
    ans = []
    for i in orders:
        for num in course:
            nPr = list(itertools.combinations(sorted(i),num))
            arr += nPr

    combi = Counter(arr).most_common()

    for num in course:
        max = 2
        for i in combi:
            if len(i[0]) == num:
                if i[1] >= max:
                    ans.append("".join(i[0]))
                    max = i[1]
                else:
                    break
            else:
                continue



    ans.sort()

    return ans