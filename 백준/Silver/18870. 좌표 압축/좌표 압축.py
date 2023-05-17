import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

sorted_arr= sorted(arr)
new_arr = dict()
new_arr[sorted_arr[0]] = 0
start = 0
for i in range(1,n):
    if sorted_arr[i-1] < sorted_arr[i]: 
        start += 1
    new_arr[sorted_arr[i]] = start

new_arr

for i in range(n):
    print(new_arr[arr[i]], end =" ")
