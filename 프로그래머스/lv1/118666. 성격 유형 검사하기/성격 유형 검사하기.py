def solution(survey, choices):
    """
    survey에 대해서 for문을 돌려 각각의 지표가 4> 4< 4 일때로 나눠서 진행

    이후 그 값을 score_dic 에 저장하여 비교, 만약 값이 같으면
    AN 은 A
    CF 는 C
    MJ 는 J
    RT 는 R 이 됨
    """
    mbti = ["RT" ,"CF" ,"JM" ,"AN"]

    score_dic = {"A":0,"C":0,"F":0,"J":0,"M":0,"N":0,"R":0,"T":0}
    for i in range(len(survey)):
        if choices[i] >  4:
            score_dic[survey[i][1]] += (choices[i] - 4)
        elif choices[i] < 4:
            score_dic[survey[i][0]] += (4 - choices[i]) 
        else:
            continue

    ans = ""
    for i in mbti:
        if score_dic[i[0]] >= score_dic[i[1]]:
            ans += i[0]
        else:
            ans += i[1]
    return ans
    