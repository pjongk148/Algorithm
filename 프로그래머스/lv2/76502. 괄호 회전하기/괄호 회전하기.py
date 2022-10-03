def check(s):
    arr = []
    
    for st in s:
        if st in ("[","(","{"):
            arr.append(st)
        else:
            if len(arr)==0:
                return False
            tmp = arr.pop()
            if st == "]" and tmp != "[":
                return False
            elif st == "}" and tmp != "{":
                return False
            elif st == ")" and tmp != "(":
                return False
    
    if len(arr) !=0:
        return False
    return True

def solution(s):
    cnt = 0
    for i in range(len(s)):
        tmp_str = s[i:] + s[:i]
        if check(tmp_str):
            cnt += 1
    return cnt