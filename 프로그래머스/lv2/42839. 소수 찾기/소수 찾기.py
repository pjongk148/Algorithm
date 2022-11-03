def solution(numbers):
    ans = []
    cnt = 0
    for i in permi(numbers,ans):
        if sosoo(i):
            cnt +=1
    return cnt

def sosoo(n):
    sosoo = True
    if n == 2:
        return sosoo
    if n % 2 == 0 or n == 1:
        return False
    
    for i in range(3,int(n**(0.5))+1,2):
        if n % i == 0:
            sosoo = False
            return sosoo
    return sosoo

def permi(n,ans):
    from itertools import permutations
    for i in range(1,len(n)+1):
        ans += [int("".join(j)) for j in permutations(list(n),i)]
    return list(set(ans))  