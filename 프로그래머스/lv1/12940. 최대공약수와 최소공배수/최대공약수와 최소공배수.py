def solution(n, m):
    num = 0
    for i in range(1,min(n,m)+1):
        if min(n,m) % i ==0 and max(n,m) % i == 0:
            num = i
    return [num,int(n*m/num)]