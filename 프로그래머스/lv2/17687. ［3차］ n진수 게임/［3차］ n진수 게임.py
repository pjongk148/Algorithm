def solution(n, t, m, p):
    jin_dic = dict()
    for i in range(0,10):
        jin_dic[i] = str(i)
    jin_dic[10] = "A"
    jin_dic[11] = "B" 
    jin_dic[12] = "C" 
    jin_dic[13] = "D" 
    jin_dic[14] = "E" 
    jin_dic[15] = "F"

    #n진법으로 숫자 변환하는 코드 작성
    def jin_soo(num,n):
        tmp = ""
        if n == 10:
            return str(num)
        else:
            while num != 0:
                tmp += jin_dic[num % n]
                num = num // n
            tmp = tmp[::-1]
            return tmp

    #튜브가 말해야 하는 숫자들이 담긴 리스트 생성
    num_arr = ['0']
    current = 0
    #튜브가 t개만큼 말하기 위해서 필요한 전체 문자열의 수 (t-1) * m + p
    while len(num_arr) != (t-1) * m + p:
        current += 1
        num_arr.append(jin_soo(current,n))

    string = " " + "".join(num_arr)
    ans = ""

    for i in range(p,(t-1) * m + p+1,m):
        ans += string[i]

    return ans