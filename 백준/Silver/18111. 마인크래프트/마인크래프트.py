from collections import Counter
import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
cnt = dict()

for _ in range(n):
    tmp = Counter(map(int,input().rstrip().split()))
    for idx in tmp.keys():
        if idx in cnt:
            cnt[idx] += tmp[idx]
        else:
            cnt[idx] = tmp[idx]
            
min_d = min(cnt.keys())
max_d = max(cnt.keys())
depth = [i for i in range(min_d,max_d+1)]
min_time = float("inf")
ans = 0

for target in depth:
    tmp_time = 0
    tmp_block = b
    for i in cnt.keys():
        dif = i - target
        if dif > 0 :
            tmp_block += dif * cnt[i]
            tmp_time += dif * 2 * cnt[i]
        elif dif < 0:
            tmp_block += dif * cnt[i]
            tmp_time -= dif * cnt[i]
                
    if tmp_block < 0:
        continue      
           
    if tmp_time <= min_time:
        min_time = tmp_time
        ans = target

print(min_time, ans)