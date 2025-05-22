def solution(N, stages):
    stages = sorted(stages)
    answer = [0 for _ in range(N)]
    
    last_v = 0
    for idx in range(N):
        if idx >= 1 and stages[idx-1] != stages[idx]:
            last_v = (idx - 1)
            answer[stages[idx-1] - 1] = last_v + 1 / N
    if last_v != N - 1:
        answer[stages[last_v] - 1] = last_v + 1 / N     
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])