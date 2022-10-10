import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) != 1 and scoville[0] < K:
        cnt += 1
        new =  heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)

    return -1 if scoville[0] < K else cnt