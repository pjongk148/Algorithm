def solution(s):
    words = [s[0]]
    for i in range(1,len(s)):
        if len(words)==0:
            words = [s[i]]
        else:
            if words[-1] == s[i]:
                words.pop()
                continue
            else:
                words.append(s[i])
    if len(words) ==0:
        return 1
    return 0