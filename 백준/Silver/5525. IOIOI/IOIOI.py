import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
st = input()
cnt = 0

point = st.index("IO")
idx = point + 0
while point <= l - (2*n+1):
    if st[idx:idx + 3] == "IOI": 
        idx += 2
        
        if idx - point == 2 * n:
            
            cnt += 1
            point += 2
    else:
        idx +=1
        point = idx + 0

print(cnt)