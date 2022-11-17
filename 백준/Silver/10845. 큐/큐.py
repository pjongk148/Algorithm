import sys

n = int(sys.stdin.readline())

queue = []

for _ in range(n):
    q = sys.stdin.readline().split()
    
    if q[0] == "push":
        queue.append(q[1])
    elif q[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif q[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif q[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif q[0] == "size":
        print(len(queue))
    elif q[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)