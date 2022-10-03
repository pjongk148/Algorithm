def solution(citations):
    n = len(citations)
    dic = {}

    for v in citations:
        if dic.get(v): dic[v] +=1
        else: dic[v] = 1

    arr = list(set(citations))

    max = 0
    cur = 0 #현재 인용수
    for i in range(arr[-1]+1): 
        if i in arr: 
            if n - cur >= i and cur <= i:
                max = i
            cur += dic[i]

        else:
            if n - cur >= i and cur <= i:
                max = i
    return max