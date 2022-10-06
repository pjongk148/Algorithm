def solution(priorities, location):
    idx_arr = [i for i in range(len(priorities))]
    ans =[]
    while priorities !=[]:
        if priorities[0] >= max(priorities):
            ans.append(idx_arr[0])
            priorities.pop(0)
            idx_arr.pop(0)

        else:
            priorities.append(priorities.pop(0))
            idx_arr.append(idx_arr.pop(0))
    return ans.index(location) + 1