from collections import Counter

alpha =["a","b","c","d","e","f","g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t","u","v","w","x","y","z"]

cnt = dict(Counter(input()))
ans = ""
for i in alpha:
    if i in cnt:
        ans += str(cnt[i]) + " "
    else:
        ans += "0 "
print(ans[:-1])