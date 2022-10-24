from itertools import combinations
def solution(numbers):
    return sorted(list(set(map(sum,combinations(numbers,2)))))