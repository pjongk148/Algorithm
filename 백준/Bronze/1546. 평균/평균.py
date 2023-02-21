N = int(input())
sum = 0
tmp = list(map(int, input().split()))
score_max = max(tmp)

for i in tmp:
    sum += i/score_max*100
ans = sum/N
print(ans)