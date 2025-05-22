
def solution(decimal):
    from collections import deque
    d = deque([])
    while decimal >= 2:
        d.appendleft(str(decimal % 2))
        decimal = decimal // 2
    if decimal == 1:
        d.appendleft(str(1))
    
    
solution(s="((()(")