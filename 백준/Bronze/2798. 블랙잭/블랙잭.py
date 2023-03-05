n, m = map(int, input().split())
card=[int(i) for i in input().split()]
arr=[]

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if card[i]+card[j]+card[k]<=m:
                arr.append(card[i]+card[j]+card[k])
                
print(max(arr))