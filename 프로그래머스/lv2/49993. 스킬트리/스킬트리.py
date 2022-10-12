def solution(skill, skill_trees):
    arr = []
    ans = len(skill_trees)

    for i in skill_trees:
        tmp = []
        for j in i:
            if j not in skill:
                continue
            tmp.append(skill.index(j))
        arr.append(tmp)

    for i in arr:
        if i != [_ for _ in range(len(i))]:
            ans -= 1

    return ans
        
    