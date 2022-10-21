def solution(s):
    s = s.lower()
    p = s.count("p")
    y = s.count("y")
    if not p and not y:
        return True
    return True if p ==y else False