def solution(A,B):
    A.sort(reverse = True)
    B.sort()
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    return sum([A[i] * B[i] for i in range(len(A))])

    