n = int(input())
books = dict()
for i in range(n):
    tmp = input().rstrip()
    if tmp in books:
        books[tmp] += 1
    else:
        books[tmp] = 1
        
books = sorted(books.items())
print(sorted(books, key = lambda x : x[1], reverse = True)[0][0])