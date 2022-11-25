n = input()
st = list("abcdefghijklmnopqrstuvwxyz")
for i in range(len(st)):
    if st[i] in n:
        st[i] = str(n.index(st[i]))
    else:
        st[i] = "-1"
        
print(" ".join(st))