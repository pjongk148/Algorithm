n = int(input())
num = [0, 1, 1]
for _ in range(3, 91):
    num.append(num[_ - 2] + num[_ - 1])
print(num[n])