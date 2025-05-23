def solution(answers):
    patterns = [
        [5, [1, 2, 3, 4, 5]],
        [8, [2, 1, 2, 3, 2, 4, 2, 5]],
        [10, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
        ]
    answer = []
    for nums_len, nums in patterns:
       answer.append((sum([ answers[i] == nums[i % nums_len] 
            for i in range(len(answers))])))
    
    max_v = max(answer)
    max_idx = []
    for idx, v in enumerate(answer):
        if v == max_v:
            max_idx.append(idx + 1)
    return max_idx

solution([1,3,2,4,2])
