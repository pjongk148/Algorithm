from itertools import product
def solution(word):
    
    p1 =  ["A","E","I","O","U"]
    word = tuple(word)
    arr = [tuple(i)for i in ["A","E","I","O","U"]]
    
    for j in range(2,6):
        arr += list(product(p1,repeat = j))
    arr.sort()
    return arr.index(word) + 1