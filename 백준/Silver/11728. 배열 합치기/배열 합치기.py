import sys
input = sys.stdin.readline
a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
ans_list = a_list + b_list
ans = ' '.join(map(str, sorted(ans_list)))
print(ans)