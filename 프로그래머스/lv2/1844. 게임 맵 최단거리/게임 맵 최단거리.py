def solution(maps):
    queue = [[0,0]]

    nx = [1,-1,0,0]
    ny = [0,0,1,-1]

    while queue:
        tmp = queue.pop(0)
        x = tmp[1]
        y = tmp[0]

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx >= 0 and dx < len(maps[0]) and dy >= 0 and dy < len(maps):
                if maps[dy][dx] == 1:
                    maps[dy][dx] = maps[y][x] + 1
                    queue.append([dy,dx])
    
    return maps[-1][-1] if maps[-1][-1] != 1 else -1