def solution(people, limit):
    people.sort()
    min =0
    max = len(people)-1
    count =0
    while min <= max:
        if people[min] + people[max] <= limit:
            min += 1
        count +=1
        max -= 1    
    return count