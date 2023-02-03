x,y = map(int, input().split())
n = list(map(int, input().split()))

for _ in n:
    if _ < y:
        print(_, end=" ")