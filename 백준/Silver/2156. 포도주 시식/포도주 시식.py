import sys
input = sys.stdin.readline

n = int(input())

# 10000으로 해주는 이유는 인덱스 크기가 작을 경우의 예외처리
arr = [0] * 10000
for i in range(n):
    arr[i] = int(input())

cnt = [0] * 10000

cnt[0] = arr[0]
cnt[1] = arr[0] + arr[1]
cnt[2] = max(cnt[1], arr[0] + arr[2], arr[1] + arr[2])

# 각각 i-1 번째 포도주, i-2 번째 포도주, i번째 포도주를 안마실 때에 해당됨
for i in range(3,n):
    cnt[i] = max(cnt[i-2] + arr[i],cnt[i-3]+ arr[i-1] + arr[i],cnt[i-1])

print(max(cnt))