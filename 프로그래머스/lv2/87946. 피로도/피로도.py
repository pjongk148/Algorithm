import itertools
def solution(k, dungeons):
    case = itertools.permutations([i for i in range(len(dungeons))], len(dungeons))
    case = list(case)

    max = 0
    for i in case:
        cur = k
        cnt = 0
        for idx in i:
            if cur >= dungeons[idx][0]:
                cur -= dungeons[idx][1]
                cnt += 1
        if max < cnt:
            max = cnt
    return max