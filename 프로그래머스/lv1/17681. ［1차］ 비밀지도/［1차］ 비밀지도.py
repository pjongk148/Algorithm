def solution(n, arr1, arr2):
    dic  = dict()
    dic[1] = "#"
    dic[0] = " "

    ans = []

    for i in range(n):
        tmp1 = bin(arr1[i])[2:]
        tmp2 = bin(arr2[i])[2:]
        tmp1 = "0" * (n- len(tmp1)) + tmp1
        tmp2 = "0" * (n- len(tmp2)) + tmp2
        st = ""
        for i in range(n):
            st += dic[int(tmp1[i]) or int(tmp2[i])]
        ans.append(st)

    return ans
    