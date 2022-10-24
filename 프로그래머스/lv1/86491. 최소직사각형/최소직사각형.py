def solution(sizes):
    """
    for 문을 돌려서 각각의 인자의 0,1값의 max 를 기록.
    만약 두개를 바꿔서비교햇을때도 max면 max값을 변경한다.
    """
    max_x = 0
    max_y = 0

    for i in sizes:
        x = min(i[0],i[1])
        y = max(i[0],i[1])

        if max_x <= x:
            max_x =x
        if max_y <= y:
            max_y = y
    return max_x * max_y