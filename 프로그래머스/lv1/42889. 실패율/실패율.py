def solution(N, stages):
    arr = [0] * (N+1)
    for i in stages:
        arr[i-1] += 1

    ans =[]
    for i in range(len(arr)-1):
        if arr[i] ==0:
            ans.append(0)
            continue
        ans.append(arr[i]/sum(arr[i:]))

    dic = dict() 
    for i,v in enumerate(ans):
        dic[i+1] = v

    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    answer = [i[0] for i in sorted_dic]
    return answer