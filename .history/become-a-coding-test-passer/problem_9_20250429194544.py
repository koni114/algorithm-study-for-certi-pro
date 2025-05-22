
def solution(decimal):
    from collections import deque
    d = deque([])
    while decimal >= 2:
        d.appendleft(decimal % 2)
        decimal = decimal // 2
    if decimal == 1:
        d.appendleft(1)
    "".join(d)
    
    
solution(s="((()(")