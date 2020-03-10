def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if participant[i] is not completion[i]:
            answer = participant[i]
        else:
            answer = participant[-1]
    return answer
