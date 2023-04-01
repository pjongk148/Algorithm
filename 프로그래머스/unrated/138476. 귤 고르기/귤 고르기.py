def solution(k, tangerine):
    arr = dict()

    for i in tangerine:
        if i in arr:
            arr[i] += 1
        else:
            arr[i] = 1

    sorted_arr = sorted(arr.values(),reverse = True)

    cnt = 0

    for i in sorted_arr:
        if k <= 0:
            break
        k -= i
        cnt += 1
    return cnt