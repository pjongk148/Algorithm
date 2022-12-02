def pibo(n):
    if n <= 1:
        return n
    if n == 2:
        return 1
    else:
        return pibo(n-1) + pibo(n-2)
    
print(pibo(int(input())))