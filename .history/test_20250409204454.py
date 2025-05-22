def solution(numbers):
    s = set()
    len_idx = len(numbers)
    for i in range(len(numbers)):
        for j in range(i+1, len_idx):
            s.add(numbers[i] + numbers[j])
    return sorted(list(s))

solution([5,0,2,7])