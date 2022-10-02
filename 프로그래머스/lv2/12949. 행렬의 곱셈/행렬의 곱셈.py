def solution(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            num =0
            for k in range(len(arr2)):
                num += arr1[i][k] * arr2[k][j]
            tmp.append(num)
        arr3.append(tmp)
    return arr3
#list(zip( * arr1 )) 행렬 뒤집기에 사용. 다음번엔 for문 여러개보다 열계산할때 사용해보자
