import sys
input =sys.stdin.readline

st = list(input().rstrip())
st2 = []

for i in range(int(input())):
    cmd = input().split()
    
    if cmd[0] == "L":
        if st:
            st2.append(st.pop())
        
    elif cmd[0] == "D":
        if st2:
            st.append(st2.pop())
        
    elif cmd[0] == "B":
        if st:
            st.pop()
    
    elif cmd[0] == "P":
        st.append(cmd[1])
    
st.extend(reversed(st2))
print("".join(st))