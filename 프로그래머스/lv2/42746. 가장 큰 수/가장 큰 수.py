def solution(numbers):
    """
    최대 1000까지 이므로 숫자에 3배를 곱해서
    문자열식 sort를 통해 큰 순서로 해준다!
"""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
    