def solution(strings, n):
    new_arr = sorted([strings[_][n] + strings[_] for _ in range(len(strings))])

    return [_[1:] for _ in new_arr]
    