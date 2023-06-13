import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))
val = dict()
idx = 0
for i in sorted_arr:
    val[i] = idx
    idx += 1

for i in range(len(arr)-1):
    print(val[arr[i]],end=" ")
    
print(val[arr[-1]])