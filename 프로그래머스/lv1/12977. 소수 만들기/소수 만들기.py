import itertools
import math
def solution(nums):
    arr = itertools.combinations(nums, 3)

    ans = list(map(sum,arr))
    cnt = 0
    for i in ans:
        print("i = " + str(i))
        if i % 2 == 0:
            continue
        else:
            tmp = True
            for j in range(3,int(math.sqrt(i))+1,2):
                if i % j == 0:
                    tmp = False
                    break
            if tmp:
                print(i)
                cnt +=1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return cnt