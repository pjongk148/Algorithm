def solution(land):
    #각각의 land[i]에 대해서 현재 인덱스를 제외한 land[i-1]의 리스트 중 큰 값을 더해줌
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[len(land)-1])