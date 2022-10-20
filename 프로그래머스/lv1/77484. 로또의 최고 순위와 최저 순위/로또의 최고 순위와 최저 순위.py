def solution(lottos, win_nums):
    dic = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1

    return [dic[cnt + lottos.count(0)],dic[cnt]]
    