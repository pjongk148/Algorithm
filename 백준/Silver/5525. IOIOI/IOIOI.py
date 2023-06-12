import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
st = input()

target = 'I' + 'OI' * n

cnt = 0
for i in range(0, len(st) - (2*n+1)+1):
    if st[i:i+(2*n+1)] == target:
        cnt += 1
print(cnt)