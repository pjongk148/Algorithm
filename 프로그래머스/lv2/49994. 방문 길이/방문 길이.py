def solution(dirs):
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