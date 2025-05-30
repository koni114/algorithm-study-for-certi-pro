def solution(participant, completion):
    from collections import defaultdict
    d = defaultdict(int)
    for name in completion:
        d[name] += 1
    for name in participant:
        if d[name] < 1:
            return name
        else:
            d[name] -= 1