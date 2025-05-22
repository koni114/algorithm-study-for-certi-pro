def solution(N, stages):
    stages = sorted(stages)
    answer = [0 for _ in range(len(N))]
    
    for idx in range(N):
        if idx >= 1 and stages[idx-1] != stages[idx]:
           answer[stages[idx-1]] = (idx - 1) / N
           
    
    
    
    return answer