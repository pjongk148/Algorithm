def solution(n):
    # one_count = bin(n)[2:].count("1")
    # min = n+1
    # for i in range(n+1,int(bin(n)+"0",2)+1):
    #     if bin(i).count("1") == one_count:
    #         return i
    cnt = bin(n).count("1")
    while True:
        n = n + 1
        if (bin(n).count("1") ==cnt):
            break
            
    return n