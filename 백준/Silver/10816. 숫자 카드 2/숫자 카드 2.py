from bisect import bisect_left, bisect_right
def count_by_range(a,left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

input()
a = input().split(" ")
a.sort()
input()
b = input().split(" ")
c = []
for i in b:
    c.append(str(count_by_range(a,i,i)))
print(" ".join(c))