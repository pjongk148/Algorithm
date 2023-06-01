import sys
input = sys.stdin.readline
import heapq

n = int(input())

arr = []

for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort()

cnt = []
heapq.heappush(cnt, arr[0][1])

for i in range(1, n):
    if arr[i][0] < cnt[0]: 
        heapq.heappush(cnt, arr[i][1])
    else:
        heapq.heappop(cnt)
        heapq.heappush(cnt, arr[i][1])

print(len(cnt))