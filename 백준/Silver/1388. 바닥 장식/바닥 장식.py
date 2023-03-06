n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input()))
    
count = 0
for i in range(n):
    a = ''
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != a:
                count += 1
        a = graph[i][j]

for j in range(m):
    a = ''
    for i in range(n):
        if graph[i][j] == '|':
            if graph[i][j] != a:
                count += 1
        a = graph[i][j]

print(count)

#dfs, bfs 개념 익히고 다시 풀어볼 것