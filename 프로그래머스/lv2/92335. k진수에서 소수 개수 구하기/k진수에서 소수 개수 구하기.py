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
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
#진수로 나타내는 함수 구현
def change_10_to_n(n, value):
    result = ''
    q, r = divmod(n, value)
    while q > 0:
        result += n_dic1[r]
        q, r = divmod(q, value)

    result += n_dic1[r]

    return result[::-1]

def solution(n,k):
    cnt = 0
    new_n = str(change_10_to_n(n,k)).split("0")
    for i in new_n:
        if i =='':
            continue
        elif sosoo(int(i)):
            cnt +=1
    return cnt