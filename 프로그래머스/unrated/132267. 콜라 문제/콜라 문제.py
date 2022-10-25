def solution(a, b, n):
    i = 0
    while (n >= a):
        i += b*(n//a)
        n = b*(n//a)+ n%a
    return i