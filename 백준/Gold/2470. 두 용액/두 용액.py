import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = n-1
cnt = 1

zero = float('inf')
ans = []

while left < right:
    min_num = arr[left]
    max_num = arr[right]
    
    total = min_num + max_num
    if abs(total) < zero:
        zero = abs(total)
        ans = [min_num,max_num]
    
    if total < 0:
        left += 1
    else:
        right -= 1
        
print(ans[0],ans[1])