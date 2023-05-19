n = int(input())
minus = []
plus = []
for i in range(n):
    tmp = int(input())
    if tmp > 0:
        plus.append(tmp)
    else:
        minus.append(tmp)


minus.sort()
plus.sort(reverse=True)


ans = 0
for i in range(len(minus)// 2):
        ans += minus[2 *i] * minus[2 *i + 1]

if len(minus) % 2 != 0:
    ans += minus[-1]
    
for i in range(len(plus)// 2):
        tmp = plus[2 *i] * plus[2 *i + 1]
        if tmp > plus[2 *i] + plus[2 *i + 1]:
            ans += tmp
        else:
            ans += plus[2 *i] + plus[2 *i + 1]
        
if len(plus) % 2 != 0:
    ans += plus[-1]
    
    
print(ans)