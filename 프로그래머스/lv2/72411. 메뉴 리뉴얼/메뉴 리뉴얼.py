import itertools
from collections import Counter
"""
조건:
1. 가장 많이 "함께" 주문된 단품메뉴의 "조합"
2. 최소 두 가지 이상 + 최소 2명 이상 주문되어야 함
각 손님은 메뉴 2개 이상 주문
"""
def solution(orders, course):
    arr = []
    ans = []
    for i in orders:
        for num in course:
            #조건 1 만족하기위한 조합(sorted(i)를 통해 문자열순서 통일)
            nPr = list(itertools.combinations(sorted(i),num))
            arr += nPr

    combi = Counter(arr).most_common()

    for num in course: #요구하는 세트메뉴 개수
        max = 2 #최소 두가지 이상 주문
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