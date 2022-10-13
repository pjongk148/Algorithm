def solution(numbers):
    """
    최대 1000까지 이므로 숫자에 3배를 곱해서
    문자열식 sort를 통해 큰 순서로 해준다!
    """
    temp = [str(_) for _ in numbers]
    temp2 =[]
    temp3 = []
    for i,v in enumerate(temp):
        temp2.append([v*3,i])

    temp2.sort(reverse=True)
    for i in temp2:
        temp3.append(temp[i[1]])

    answer = str(int("".join(temp3)))
    return answer
    