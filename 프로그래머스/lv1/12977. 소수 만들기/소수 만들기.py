from itertools import combinations
import math
def solution(nums):
    arr = list(map(sum,combinations(nums, 3)))
    cnt = len(arr)
    for i in arr:
        if i % 2 == 0:
            cnt -=1
        else:
            for j in range(3,int(math.sqrt(i))+1,2):
                if i % j == 0:
                    cnt -=1
                    break
    return cnt