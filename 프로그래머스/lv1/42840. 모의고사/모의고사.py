def solution(answers):
    num1 = [1,2,3,4,5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0,0,0]
    ans =[]
    for idx, answer in enumerate(answers):
        if answer == num1[idx%len(num1)]:
            cnt[0] += 1
        if answer == num2[idx%len(num2)]:
            cnt[1] += 1
        if answer == num3[idx%len(num3)]:
            cnt[2] += 1

    for idx, s in enumerate(cnt):
        if s == max(cnt):
            ans.append(idx+1)

    return ans