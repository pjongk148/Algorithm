def solution(msg):
    alpha = dict()
    for i in range(65,91):
        alpha[chr(i)] = i -64

    stack = []
    msg = list(msg)
    word = msg.pop(0)
    cur_num = 27

    while msg:
        if word in alpha:
            word += msg.pop(0)

        else:
            stack.append(alpha[word[:-1]])
            alpha[word] = cur_num
            cur_num +=1
            word = word[-1]

    if word in alpha:
            stack.append(alpha[word]) 

    else:
        alpha[word] = cur_num
        stack.append(alpha[word[:-1]])
        stack.append(alpha[word[-1]])
    return stack