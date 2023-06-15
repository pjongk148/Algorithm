import sys
input = sys.stdin.readline

grade = {"A+": 4.5, "A0": 4.0,
             "B+": 3.5, "B0": 3.0,
             "C+": 2.5, "C0": 2.0,
             "D+": 1.5, "D0": 1.0,
             "F": 0.0}

result = 0
total = 0

for _ in range(0, 20, 1):
    tmp = input().split()

    if tmp[2] == "P":
        continue

    total += float(tmp[1])
    result += float(tmp[1]) * grade[tmp[2]]

ans = result / total


print(format(ans, '.6f'))