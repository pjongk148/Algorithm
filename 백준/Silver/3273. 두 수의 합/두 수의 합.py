import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x= int(input())
nums = dict()
for i in arr:
    nums[i] = True

ans = 0
for i in arr:
    if (x-i) in nums:
        ans += 1

print(ans // 2)