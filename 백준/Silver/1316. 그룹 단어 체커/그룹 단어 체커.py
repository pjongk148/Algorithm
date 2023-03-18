cnt = 0
for _ in range(int(input())):
    words = []
    word = input()
    words.append(word[0])
    for i in range(1,len(word)):
        if word[i] == word[i-1]:
            continue
        else:
            if word[i] in words:
                cnt -= 1
                break
            else:
                words.append(word[i])
    cnt += 1
print(cnt)