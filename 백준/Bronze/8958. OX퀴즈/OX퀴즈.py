for _ in range(int(input())) :
    tmp = list(input())
    score = 0
    total_score = 0
    for i in tmp :
        if i == 'O' :
            score += 1
            total_score += score
        else :
            score = 0
    print(total_score)