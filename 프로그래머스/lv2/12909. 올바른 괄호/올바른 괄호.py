def solution(s):
    if s[0] == ")":
        return False
    start = 0
    end = 0
    for str in s:
        if end > start:
            return False
        else:
            if str == "(":
                start += 1
            else:
                end += 1
    return start == end