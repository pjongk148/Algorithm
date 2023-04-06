import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
card_list = Counter(input().split())

m = int(input())
test_list = input().split()

print(' '.join(str(card_list[i]) for i in test_list))