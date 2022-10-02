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