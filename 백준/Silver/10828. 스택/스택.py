import sys
input = sys.stdin.readline

n = int(input())
stack = []

def st(cmd):
    tmp = cmd.split()
    if tmp[0] == "push":
        stack.append(int(tmp[1]))
        
    if tmp[0] == "top": 
        if stack:
            print(stack[-1])
        else:
            print(-1)
            
    if tmp[0] == "size":
        print(len(stack))
        
    if tmp[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
                  
    if tmp[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    
for _ in range(n):
    st(input())