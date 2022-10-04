from math import ceil
def solution(progresses, speeds):
    ans = []
    tmp =1
    max =ceil((100-progresses[0]) / speeds[0])
    for i in range(1,len(progresses)):
        if ceil((100-progresses[i]) / speeds[i]) > max:
            max = ceil((100-progresses[i]) / speeds[i])
            ans.append(tmp)
            tmp =1
        else:
            tmp += 1

    ans.append(tmp)
    return ans