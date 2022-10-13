def solution(dirs):
    """
우선 cur변수를 통해 좌표평면을 지정하고 for문으로 dirs를 순회한다
각각의 값에 따라 dirs[0], dirs[1]을 선택하고 빼거나 더해준다
x와 y의절대값이 5이상이 되면 continue 해준다
방문한 점은 visited 리스트에 담아준다

+++ 좌-> 우, 우 -> 좌 위 -> 아래, 아래-> 위 동일한거 추가!
"""
    x= 0
    y=0
    visited =[]
    cnt =0
    for arrow in dirs:
        tmp_x = x
        tmp_y = y
        if arrow == "U":
            y += 1
        if arrow == "D":
            y -= 1
        if arrow == "L":
            x -= 1
        if arrow == "R":
            x += 1
        
        if abs(x) > 5 or abs(y) > 5:
            x = tmp_x
            y = tmp_y
            continue
        if [[tmp_x,tmp_y],[x,y]] in visited or [[x,y],[tmp_x,tmp_y]] in visited:
            continue
        visited.append([[tmp_x,tmp_y],[x,y]])
        cnt +=1
    return cnt