def solution(arr, target):
    import itertools
    for a, b in itertools.combinations(arr, 2):
        if a + b == target:
            return True
    return False

solution([2, 3, 5, 9], 10)

def solution(arr, target):
    d = {i: 1 for i in arr}
    for v in arr:
        del d[v]
        if target - v in d:
            return True
        d[v] = 1
    return False