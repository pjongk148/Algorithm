import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
visited = [[False] * m for _ in range(n)]
x = -1
y = -1
for i in range(n):
    arr.append(list(input()))
    if "I" in arr[i]:
        x = i
        y = arr[i].index("I")

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = [[x,y]]
ans = 0

while queue:
    x,y = queue.pop()
    
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
            
        else:
            if not visited[nx][ny]:

                if arr[nx][ny] == "P":
                    ans += 1
                    visited[nx][ny] = True
                    queue.append([nx,ny])

                elif arr[nx][ny] == "O":
                    visited[nx][ny] = True
                    queue.append([nx,ny])

print(ans) if ans > 0 else print("TT")