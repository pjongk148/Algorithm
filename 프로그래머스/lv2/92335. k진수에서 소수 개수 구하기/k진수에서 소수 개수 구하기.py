"""
다른 사람의 풀이(훨씬 간단하고 가독성 좋음)
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt
"""





#소수인지 판별하는 함수 구현
import math
def sosoo(n):
    if n ==1:
        return False
    if n ==2:
        return True
    if n % 2 ==0:
        return False
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n % i == 0:
                return False
    return True

n_dic1 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
}
#진수로 나타내는 함수 구현
def jinsoo(n, value):
    result = ''
    q, r = divmod(n, value)
    while q > 0:
        result += n_dic1[r]
        q, r = divmod(q, value)

    result += n_dic1[r]

    return result[::-1]

def solution(n,k):
    cnt = 0
    new_n = str(jinsoo(n,k)).split("0")
    for i in new_n:
        if i =='':
            continue
        elif sosoo(int(i)):
            cnt +=1
    return cnt