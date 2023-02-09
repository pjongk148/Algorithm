tmp1 = int(input())
tmp2 = int(input())
tmp3 = int(input())

ans = list(str(tmp1 * tmp2 * tmp3))
for _ in range(10):
    print(ans.count(str(_)))