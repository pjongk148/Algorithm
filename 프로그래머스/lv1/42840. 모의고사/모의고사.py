def solution(answers):
    ans_1 = [1,2,3,4,5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]
    ans_1 = ans_1 * (len(answers) // 5) + ans_1[:len(answers) % 5]
    ans_2 = ans_2 * (len(answers) // 5) + ans_2[:len(answers) % 5]
    ans_3 = ans_3 * (len(answers) // 5) + ans_3[:len(answers) % 5]

    ans = []
    for i in range(len(answers)):
        if ans_1[i] == answers[i]:
            count[0]+=1
        if ans_2[i] == answers[i]:
            count[1]+=1
        if ans_3[i] == answers[i]:
            count[2]+=1

    for i in range(len(count)):
        if count[i] == max(count):
            ans.append(i+1)
    return ans