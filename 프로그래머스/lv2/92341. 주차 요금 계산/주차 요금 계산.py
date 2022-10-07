import math
def solution(fees, records):
    # 우선 차량번호 별로 묶어서 dict 형식으로 변환
    # 먼저 차량번호 + 숫자
    car_time = {}
    for i in records:
        tmp = i.split(" ")
        if tmp[1] not in car_time:
            car_time[tmp[1]] = [tmp[0]]
        else:
            car_time[tmp[1]].append(tmp[0])
            
    #차량별 정리된 시간 합치기 - 출차 안한경우(len이 홀수) 23:59 더해주기
    time = dict()
    for i in car_time:
        time[i] = 0
        if len(car_time[i]) % 2 != 0:
            car_time[i].append("23:59")
        for time_idx in range(0,len(car_time[i]),2):
            tmp_time = 60 * (int(car_time[i][time_idx+1][:2]) - int(car_time[i][time_idx][:2])) + (int(car_time[i][time_idx+1][3:]) - int(car_time[i][time_idx][3:]))
            time[i] += tmp_time
    
    
    #시간에 따른 요금 계산
    answer = []
    for i in sorted(list(time.keys())):
        if time[i] <=  fees[0]:
            answer.append(fees[1])
        else:
            extra = time[i] - fees[0]
            answer.append(math.ceil(extra / fees[2]) * fees[3] + fees[1])
    
            
            
    return answer