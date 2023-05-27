arr= dict()
for i in range(8):
    arr[i+1] = int(input())
ans = sorted(arr.items(), key= lambda x:x[1], reverse=True)
ans1 = 0
ans2 = []

for i in range(5):
    ans1 += ans[i][1]
    ans2.append(ans[i][0])
print(ans1)
ans2.sort()
for i in ans2:
    print(i, end= ' ')