def solution(a, b):
    answer = 0
    if a>b:
        temp = a
        a = b
        b =temp
    b_sum = b*(b+1)/2
    a_sum = (a-1)*a/2
    answer = b_sum - a_sum
    return answer
    