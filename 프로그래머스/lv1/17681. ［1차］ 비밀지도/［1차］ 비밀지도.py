def solution(n, arr1, arr2):
    dic  = dict()
    dic[1] = "#"
    dic[0] = " "

    ans = []
    #n번 만큼 순회하면서 2진수 형태로 arr요소를 변경
    for i in range(n):
        tmp1 = bin(arr1[i])[2:]
        tmp2 = bin(arr2[i])[2:]
        #부족한 길이만큼 0을 채워준다
        tmp1 = "0" * (n- len(tmp1)) + tmp1
        tmp2 = "0" * (n- len(tmp2)) + tmp2
        st = ""
        #반복문을 한번 더 돌면서 1 or 0 =0을 이용하여 str생성 후 ans에 담아준 뒤 반환
        for i in range(n):
            st += dic[int(tmp1[i]) or int(tmp2[i])]
        ans.append(st)

    return ans
    