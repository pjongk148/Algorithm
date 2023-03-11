m,n = map(int, input().split())

arr = set([])
cnt = 0

for m in range(m):
    tmp = input().rstrip()
    arr.add(tmp)
   
for n in range(n):
    tmp = input().rstrip()
    if tmp in arr:
        cnt += 1

print(cnt)