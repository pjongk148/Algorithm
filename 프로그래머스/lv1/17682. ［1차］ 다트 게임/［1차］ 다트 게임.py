def solution(dartResult):
        score =[]
        for i,v in enumerate(dartResult):
            if v == "0" and dartResult[i-1] == "1":
                score[-1] = 10
            elif v.isdigit():
                score.append(int(v))
            elif v == "D":
                score[-1] **= 2
            elif v == "T":
                score[-1] **= 3
            elif v == "*":
                score[-1] *= 2
                if len(score) > 1:
                    score[-2] *= 2
            elif v == "#":
                score[-1] = -score[-1]
        return sum(score)