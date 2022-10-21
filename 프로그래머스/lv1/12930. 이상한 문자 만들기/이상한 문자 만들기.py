def solution(s):
    arr = s.split(" ")
    back = [True, False]
    ans = []

    for i in range(len(arr)):
        for _ in range(len(arr[i])):
            if back[_ % 2]:
                ans.append(arr[i][_].upper())
            else:
                ans.append(arr[i][_].lower())
        ans.append(" ")
    return "".join(ans)[:-1]