def solution(s):
    arr = list(s[2:-2].split("},{"))
    arr.sort(key=len)

    tmp_list =[]
    for i in arr:
        i = i.split(",")
        for st in i:
            if int(st) in tmp_list:
                continue
            else:
                tmp_list.append(int(st))
    return tmp_list