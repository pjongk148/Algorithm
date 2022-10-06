def solution(priorities, location):
    if len(priorities) ==1:
        return 1

    count = 0 
    order = [i for i in range(0,len(priorities))]
    while priorities:
        if priorities[0] >= max(priorities):
            count +=1
            if order[0] == location:

                return count
                break
            else:
                priorities.pop(0)
                order.pop(0)

        else:
            priorities.append(priorities.pop(0))
            order.append(order.pop(0))
            
    return count