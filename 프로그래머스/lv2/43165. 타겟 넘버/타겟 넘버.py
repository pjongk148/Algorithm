def solution(numbers, target):
    answer =0
    arr = [0]
    for num in numbers:
        tmp = []
        for i in arr:
            tmp.append(i + num)
            tmp.append(i - num)
        arr = tmp
    for _ in arr:
        if _ == target:
            answer += 1
    return answer