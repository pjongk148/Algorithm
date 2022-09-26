def solution(s):
    cnt = 0
    zero_cnt = 0
    while (s != "1"):
        cnt += 1
        zero_cnt += len(s) - len(s.replace("0",""))
        s = bin(len(s.replace("0","")))[2:]
        
    return [cnt,zero_cnt]