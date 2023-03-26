import sys

n = int(sys.stdin.readline())
hand_card = set(map(int, sys.stdin.readline().split()))
# hand_card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

for i in num:
  if i in hand_card:
    print(1, end=' ')
  else:
    print(0, end=' ')