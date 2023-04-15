n = int(input())
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))
for i in people:
    ranking = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            ranking += 1
    print(ranking, end=" ")