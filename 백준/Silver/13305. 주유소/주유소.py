import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = price[0] * dist[0]
cur_price = price[0]
for i in range(1,n-1):
    if price[i] < cur_price:
        cur_price = price[i]
    
    ans += cur_price * dist[i]
print(ans)