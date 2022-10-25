def solution(s):
    min_len = len(s)

    for i in range(1,len(s)//2+1):
        ans = ""
        cnt = 1
        queue = s[:i]
        new_s = s[i:]
        new_s += " " *(i - len(s) % i)
        while new_s:
            if queue == new_s[:i]:
                cnt += 1
                new_s = new_s[i:]
            else:
                if cnt != 1:
                    ans += str(cnt) + queue
                else:
                    ans += queue
                queue = new_s[:i]
                new_s = new_s[i:]
                cnt = 1

        if cnt != 1:
            ans += str(cnt)
        ans += queue
        ans = ans.replace(" ","")
        if len(ans) <= min_len:
            min_len = len(ans)
    return min_len