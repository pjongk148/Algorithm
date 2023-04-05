import sys
input=sys.stdin.readline

def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
target_arr = list(map(int, input().split()))

m = int(input())
test_arr = list(map(int, input().split()))

target_arr.sort()

for i in test_arr:
    print(binary_search(target_arr,i,0,len(target_arr)-1))