n=int(input())
for i in range(n):
    count,s = list(map(str,input().split()))
    for j in range(len(s)):
        print(s[j]*int(count),end='')
    print()