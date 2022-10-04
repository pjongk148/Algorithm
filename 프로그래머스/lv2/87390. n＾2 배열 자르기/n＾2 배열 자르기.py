def solution(n, left, right):
    ans =[]
    cur =0
    for i in range(1,n+1):
        cur += n
        if cur <= left:
            left -= n
            right -= n
            cur =0
            continue
        else:
            tmp = [i] * i + [i for i in range (i+1,n+1)]
            ans += tmp
            if cur >= right:
                break
    
    return ans[left:right+1]