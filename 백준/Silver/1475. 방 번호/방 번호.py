from collections import Counter

n = input()
n = n.replace('6','9')
cnt = Counter(n)
tmp = cnt['9']
cnt['9'] = tmp // 2 + tmp % 2
print(sorted(cnt.items(), key=lambda x: x[1],reverse = True)[0][1])