"""
새로 알게된 점
중요한 것은 str의 isalpha() 라는 메서드
s[1:]를 만들어 zip을 이용해 추출하는 방법

"""
import math

def get_set(s):
    list_ = list()
    for c1, c2 in zip(s, s[1:]):
        new = str(c1 + c2).lower()
        if new.isalpha():
            list_.append(new)
    return list_

def solution(str1, str2):
    # 1. 문자열 끊기
    list_1 = get_set(str1)
    list_2 = get_set(str2)
    if len(list_1) == 0 and len(list_2) == 0:
        answer = 1
    else:
        # 2. 교집합, 합집합 구하기
        inter = set(list_1) & set(list_2)
        uni = set(list_1) | set(list_2)
        # 3. 다중집합 구하기
        inter_list = [min(list_1.count(i), list_2.count(i)) for i in inter]
        uni_list = [max(list_1.count(i), list_2.count(i)) for i in uni]

        answer = sum(inter_list) / sum(uni_list)
    answer = math.trunc(answer * 65536)
    return answer