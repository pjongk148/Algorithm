def solution(n):
    st = ""

    while n!=0:
        st += str(n % 3)
        n = n // 3

    return sum([int(st[i]) * (3**(len(st)-1-i)) for i in range(len(st))])