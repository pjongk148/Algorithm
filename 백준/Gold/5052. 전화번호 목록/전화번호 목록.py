import sys

n = int(sys.stdin.readline())
for _ in range(n):
    t = int(sys.stdin.readline())
    arr = [str(sys.stdin.readline().strip()) for _ in range(t)]
    ans = "YES"
    
    arr.sort()
    for i in range(1,t):
        if arr[i-1] == arr[i][:len(arr[i-1])]:
            ans = "NO"
            break
    print(ans)