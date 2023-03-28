n, m = map(int, input().split())
trees = list(map(int, input().split()))

s, e = 1, sum(trees)

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    
    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    if cnt >= m:
        s = mid + 1
    else:
        e = mid - 1
print(e)