import sys
arr = []
for i in range(int(sys.stdin.readline())):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
arr.sort()

for i in arr:
    print(i[0],i[1])