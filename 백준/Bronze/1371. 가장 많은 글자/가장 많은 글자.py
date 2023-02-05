import sys
word = 'abcdefghijklmnopqrstuvwxyz'
result = []
txt = sys.stdin.read()

for i in word:
    result.append(txt.count(i))

m = max(result)
for i in range(len(result)):
    if m == result[i]:
        print(chr(i+97), end = '')