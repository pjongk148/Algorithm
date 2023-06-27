import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
min_dep  = 101
max_dep = 0

arr = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    if min(tmp) < min_dep:
        min_dep = min(tmp)
    if max(tmp) > max_dep:
        max_dep = max(tmp)
    arr.append(tmp)

water = [[False]* n for _ in range(n)]
max_cnt = 1

for depth in range(min_dep,max_dep):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if not water[i][j] and arr[i][j] > depth:
                queue = deque()
                queue.append((i,j))
                water[i][j] = True
                while queue:
                    x,y = queue.pop()

                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx = x + dx
                        ny = y + dy
                        if nx >= 0 and ny >= 0 and nx < n and ny < n:
                            if not water[nx][ny]:
                                if arr[nx][ny] > depth:
                                    water[nx][ny] = True
                                    queue.append((nx,ny))

                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
    water = [[False] * n for _ in range(n)]
    
print(max_cnt)             