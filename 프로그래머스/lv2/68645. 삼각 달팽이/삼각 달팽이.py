def solution(n):
    tmp = [[0] * n for _ in range(n)]
    ans = []
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:      
                x += 1          
            elif i % 3 == 1:    
                y += 1            
            elif i % 3 == 2:    
                x -= 1
                y -= 1      
            tmp[x][y] = num
            num += 1
            
    for i in tmp:
        for j in i:
            if j:
                ans.append(j)
    return ans