import heapq
import sys 
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    heapq.heappush(arr,int(input()))
ans = 0
while len(arr) != 1:
    tmp1 = heapq.heappop(arr)
    tmp2 = heapq.heappop(arr)
    heapq.heappush(arr, tmp1 + tmp2)
    ans += tmp1 + tmp2
print(ans)