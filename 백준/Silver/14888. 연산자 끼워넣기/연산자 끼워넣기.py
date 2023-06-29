import sys
import copy
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
plus,minus,multi,divide = map(int, input().split())

idx = 1
start = arr[0]
ans_arr = []

def backtrack(idx,ans, plus, minus, multi, divide):
    if idx == n:
        ans_arr.append(ans)
        return
    else:
        if plus:
            backtrack(idx+1,ans + arr[idx],plus-1,minus,multi,divide)
        if minus:
            backtrack(idx+1,ans - arr[idx],plus,minus-1,multi,divide)
        if multi:
            backtrack(idx+1,ans * arr[idx],plus,minus,multi-1,divide)
        if divide:
            if ans < 0:
                backtrack(idx+1,-(-ans // arr[idx]),plus,minus,multi,divide-1)
            else:
                backtrack(idx+1,ans // arr[idx],plus,minus,multi,divide-1)

backtrack(idx,start,plus,minus,multi,divide)

print(max(ans_arr))
print(min(ans_arr))