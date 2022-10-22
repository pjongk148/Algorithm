def solution(n):
    st = ""

    while n!=0:
        st += str(n % 3)
        n = n // 3

    return int(st,3)