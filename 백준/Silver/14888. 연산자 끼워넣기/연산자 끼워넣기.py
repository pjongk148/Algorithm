import sys
import copy
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

tmp = list(map(int, input().split()))
calc =[]

idx = 1
ans = arr[0]
ans_arr = []


def backtrack(arr, tmp,idx, ans):
    
    if idx ==len(arr):
        ans_arr.append(ans)
        return

    for i in range(0,4):
        cal = arr[idx]
        if tmp[i] > 0:
            if i == 0:
                new_tmp = copy.deepcopy(tmp)
                new_tmp[i] -= 1
                
                backtrack(arr,new_tmp,idx+1,ans + cal)
            elif i == 1:
                new_tmp = copy.deepcopy(tmp)
                new_tmp[i] -= 1
                
                backtrack(arr,new_tmp,idx+1,ans - cal)
            elif i == 2:
                new_tmp = copy.deepcopy(tmp)
                new_tmp[i] -= 1
                
                backtrack(arr,new_tmp,idx+1,ans * cal)
            else:
                new_tmp = copy.deepcopy(tmp)
                new_tmp[i] -= 1
                
                if ans < 0:
                    backtrack(arr,new_tmp,idx+1,-(-ans // cal))

                else:
                    backtrack(arr,new_tmp,idx+1,ans // cal)

backtrack(arr, tmp,idx, ans)

print(max(ans_arr))
print(min(ans_arr))