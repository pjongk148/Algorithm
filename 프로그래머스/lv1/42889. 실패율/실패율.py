def solution(N, stages):
    stages.sort(reverse=True)
    capacity = {}
    for i in range(1,N+1):
        if i not in stages:
            capacity[i] = 1
            
        else:
            capacity[i] = 1 - (stages.count(i)/(stages.count(i) + stages.index(i)))

    sorted_dict = sorted(capacity.items(), key = lambda item: item[1])
    answer = [i[0] for i in sorted_dict]
    return answer