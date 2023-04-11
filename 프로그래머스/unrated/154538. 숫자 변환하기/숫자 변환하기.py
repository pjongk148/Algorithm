def solution(x, y, n):
    answer = 0
    DP = [y + 1] * (y+1)
    DP[x] = 0
    
    for i in range(x+1, y+1):
        if i < x+n and i < 2*x:
            continue
            
        DP[i] = min(DP[i-n]+1, DP[i])
        
        if i%2==0:
            DP[i] = min(DP[i], DP[i//2]+1)
        
        if i%3==0:
            DP[i] = min(DP[i], DP[i//3]+1)

    return DP[y] if DP[y] != y + 1 else -1