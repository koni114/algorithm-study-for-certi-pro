def solution(N, k):
    from collections import deque
    d = deque([i for i in range(1, N+1)])
    
    while len(d) > 1:
        tmp_k = k - 1
        while tmp_k:
            tmp_v = d.popleft()
            d.append(tmp_v)
            tmp_k -= 1
        print(d.popleft())
    
    return d.popleft()

solution(5, 2)