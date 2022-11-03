def solution(bridge_length, weight, truck_weights):
    bridge = [0 for _ in range(bridge_length-1)]
    bridge.append(truck_weights.pop(0))
    cnt = 1
    while truck_weights:
        cnt += 1
        bridge.pop(0)
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    return cnt + len(bridge)