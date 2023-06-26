import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    sta = n * 0.15
    if sta - int(sta) >= 0.5:
        sta = int(sta) +1
    else:
        sta = int(sta)

    ans = sum(arr[sta:n-sta]) / len(arr[sta:n-sta])

    print(int(ans) +1) if ans - int(ans) >= 0.5 else print(int(ans))