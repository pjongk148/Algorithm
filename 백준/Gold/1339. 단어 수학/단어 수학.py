n = int(input())
word_list = []
arr = dict()
for i in range(n):
    word = input()
    word_list.append(word)
    
    for i in range(len(word)):
        if word[i] in arr:
            arr[word[i]] += 10**(len(word) -(i+1))
        else:
            arr[word[i]] = 10 ** (len(word) -(i+1))
ans = "+".join(word_list)

arr = sorted(arr.items(), key=lambda x: x[1],reverse=True)

for i in range(len(arr)):
    ans = ans.replace(arr[i][0],str(9-i))

print(eval(ans))