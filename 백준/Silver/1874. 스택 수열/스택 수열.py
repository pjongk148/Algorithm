import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
n_arr = []
ans = []
idx = 0
point = 1

def stack(n,arr,n_arr,ans,idx,point):
    while idx < n:
        target = arr[idx]
        if point < target:
            for i in range(point,target):
                n_arr.append(i)
                ans.append("+")
            ans.append("+")
            ans.append("-")
            point = target + 1
        elif point == target:
            ans.append("+")
            ans.append("-")
            point = target + 1
        else:
            if not n_arr or n_arr[-1] <target:
                print("NO")
                break
            else:
                while True:
                    tmp = n_arr.pop()
                    ans.append("-")
                    if tmp == target:
                        break

        idx += 1

    if idx == n:
        for i in ans:
            print(i)

stack(n,arr,n_arr,ans,idx,point)