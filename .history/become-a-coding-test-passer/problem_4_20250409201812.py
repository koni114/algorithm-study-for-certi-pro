def solution(answers):
    patterns = [
        [5, [1, 2, 3, 4, 5]],
        [8, [2, 1, 2, 3, 2, 4, 2, 5]],
        [10, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
        ]
    answer = []
    for idx, nums_len, nums in enumerate(patterns):
       answer.append((sum([ answers[i] == nums[i % nums_len] 
            for i in range(len(answers))])), idx)
    
    print(answer)
    return answer

solution([1, 2, 3, 4, 5])
