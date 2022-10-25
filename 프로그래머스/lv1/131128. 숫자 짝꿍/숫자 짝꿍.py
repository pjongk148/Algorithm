def solution(x, y):
    inter = set(x) & set(y)
    if not inter:
        return "-1"
    if inter == {"0"}:
        return "0"
    
    total = []

    for i in inter:
        for _ in range(min(x.count(i),y.count(i))):
            total.append(i)

    total.sort(reverse=True)

    
    return "".join(total)