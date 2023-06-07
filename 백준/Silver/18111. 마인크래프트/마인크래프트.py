import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())

arr = [list(map(int,input().rstrip().split())) for _ in range(n)]

min_d = 257
max_d = 0
for i in arr:
    if max_d < max(i):
        max_d = max(i)
    if min_d > min(i):
        min_d = min(i)

depth = [i for i in range(min_d,max_d+1)]
min_time = float("inf")
ans = 0
for target in depth:
    tmp_time = 0
    tmp_block = b
    for i in range(n):
        for j in range(m):
            dif = arr[i][j] - target
            if dif > 0 :
                tmp_block += dif
                tmp_time += dif * 2
            elif dif < 0:
                tmp_block += dif
                tmp_time -= dif
                
    if tmp_block < 0:
        continue      
           
    if tmp_time <= min_time:
        min_time = tmp_time
        ans = target

print(min_time, ans)