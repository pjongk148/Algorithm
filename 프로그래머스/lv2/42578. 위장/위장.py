def solution(clothes):
    dic = {}
    ans = 1

    for v,k in clothes:
        if k in dic:
            dic[k].append(v)
        else:
            dic[k] = [v]

    for i in list(dic.keys()):
        ans *= (len(dic[i]) +1)
    return ans -1