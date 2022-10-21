def solution(numbers, hand):
    num = {}
    num[1] = (0,0)
    num[2] = (0,1)
    num[3] = (0,2)
    num[4] = (1,0)
    num[5] = (1,1)
    num[6] = (1,2)
    num[7] = (2,0)
    num[8] = (2,1)
    num[9] = (2,2)
    num[0] = (3,1)

    cur_left = (3,0)
    cur_right = (3,2)
    
    ans = []
    for i in numbers:
        if i == 5:
            print(i, cur_left, cur_right)
        if i == 1 or i == 4 or i == 7:
            ans.append("L")
            cur_left = num[i]
        elif i == 3 or i == 6 or i == 9:
            ans.append("R")
            cur_right = num[i]

        else:
            left_far =  abs(num[i][0] - cur_left[0]) + abs(num[i][1] - cur_left[1])
            right_far =  abs(num[i][0] - cur_right[0]) + abs(num[i][1] - cur_right[1]) 
            if left_far < right_far:
                ans.append("L")
                cur_left = num[i]
            elif left_far > right_far:
                ans.append("R")
                cur_right = num[i]
            else:
                if hand == "right":
                    ans.append("R")
                    cur_right = num[i]
                else:
                    ans.append("L")
                    cur_left = num[i]
    return "".join(ans)