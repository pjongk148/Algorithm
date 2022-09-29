from math import gcd
def solution(arr):
    max = arr[0] * arr[1] / gcd(arr[0],arr[1])
    for i in range(2,len(arr)):
        max = arr[i] * max / gcd(arr[i],int(max))
    return max