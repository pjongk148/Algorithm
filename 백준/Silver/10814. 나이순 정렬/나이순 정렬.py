n = int(input())
users = []

for i in range(n):
    user_age, user_name = map(str, input().split())
    user_age = int(user_age)
    users.append((user_age, user_name))

users.sort(key = lambda age: (age[0]))

for i in users:
    print(i[0], i[1])