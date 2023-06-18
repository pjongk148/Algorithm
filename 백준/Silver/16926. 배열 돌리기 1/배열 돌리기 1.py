import sys
import math
input = sys.stdin.readline

n,m,r = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(n)]

def rotate(x,y,z,w):
    if x* 2 >= z or y * 2>= w:
        return
    
    tmp = arr[z-x][y]
    tmp2 = arr[x][w-y]
    
    for i in range(z-x-1,x-1,-1):
        arr[i+1][y] = arr[i][y]
    
    for i in range(x,z-x):
        arr[i][w-y] = arr[i+1][w-y]
    
    arr[z-x][y+1:w-y+1] = [tmp] + arr[z-x][y+1:w-y]
    arr[x][x:w-y] = arr[x][y+1:w-y] + [tmp2]
    
    x += 1
    y += 1
    
    rotate(x,y,z,w)
    
for i in range(r):
    rotate(0,0,len(arr)-1,len(arr[0])-1)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end= " ")
    print()   