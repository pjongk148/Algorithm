def solution(prices):
    count = 0
    answer =[]
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            count +=1
            if prices[i] > prices[j]:
                break

        answer.append(count) 
        count = 0

    answer.append(0)
    return answer