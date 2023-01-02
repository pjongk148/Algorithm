hour, min = map(int, input().split())
num = int(input()) 

hour += num // 60
min += num % 60

if min >= 60:
    hour += 1
    min -= 60
if hour >= 24:
    hour -= 24

print(hour,min)