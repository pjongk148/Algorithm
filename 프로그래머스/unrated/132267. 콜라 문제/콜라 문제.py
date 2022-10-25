def solution(a, b, n):
    i = 0
    while (n >= a):
        print(i, n)
        i += bottle(a,b,n)[0]
        n = bottle(a,b,n)[0] + bottle(a,b,n)[1]
    return i

def bottle(a,b,n):
    return [b*(n//a),n%a]