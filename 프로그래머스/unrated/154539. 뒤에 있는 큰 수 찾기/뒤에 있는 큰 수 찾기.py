def solution(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    for i, val in enumerate(numbers):
        while stack and numbers[stack[-1]] < val:
            answer[stack.pop()] = val
        stack.append(i)
    return answer