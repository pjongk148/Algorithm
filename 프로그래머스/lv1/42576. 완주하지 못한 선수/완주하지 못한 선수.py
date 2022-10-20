def solution(participant, completion):
    if set(participant) - set(completion):
        return list(set(participant) - set(completion))[0]
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
        
    
    
    