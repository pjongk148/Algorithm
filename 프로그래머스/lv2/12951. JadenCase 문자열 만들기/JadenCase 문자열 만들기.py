def solution(s):
    str = s[0].upper()
    for i in range(1,len(s)):
        if (s[i-1] == " " and s[i] != " "):
            str += s[i].upper()
        else:
            str += s[i].lower()
    return str