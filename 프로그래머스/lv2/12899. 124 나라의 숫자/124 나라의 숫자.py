def solution(n):
    ans = ''
    while n>0:
        if n % 3 == 0:
            ans += "4"
            n = n//3 -1
        else:
            ans += str(n % 3)
            n //= 3
    return ans[::-1]