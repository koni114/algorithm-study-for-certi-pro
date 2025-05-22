
def solution(v):
    from collections import deque
    d = deque([])
    while v >= 2:
        d.appendleft(v % 2)
        v = v // 2
    if v == 1:
        d.appendleft(1)
    return "".join(d)
    
    
solution(v=10)