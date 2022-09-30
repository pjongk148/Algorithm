import math
def solution(n,a,b):
    num =1
    if (a<b):
        while a % 2 ==0 or a+1!=b:
            a = math.ceil(a/2)
            b = math.ceil(b/2)
            num +=1
        return num
    else:
        while b % 2 ==0 or b+1!=a:
            a = math.ceil(a/2)
            b = math.ceil(b/2)
            num +=1
        return num