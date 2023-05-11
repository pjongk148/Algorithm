x,target = map(int,input().split())

min_cnt = float("inf")
def dfs(x,target,cnt):
    global min_cnt
    if x == target:
        if cnt < min_cnt:
            min_cnt = cnt
            return
    elif x > target:
        return
    else:
        if target % 2 == 0:
            dfs(x,target//2,cnt+1)
        tmp = str(target)
        if  tmp[-1] == '1':
            dfs(x,int(tmp[:-1]),cnt+1)

dfs(x,target,1)
print(min_cnt if min_cnt != float("inf") else -1)