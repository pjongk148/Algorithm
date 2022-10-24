from itertools import combinations
def solution(number):
    return list(map(sum,combinations(number,3))).count(0)