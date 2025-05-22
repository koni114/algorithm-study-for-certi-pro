
def solution(decimal):
    from collections import deque
    d = deque([])
    while decimal >= 2:
        d.appendleft(str(decimal % 2))
        decimal = decimal //2 
    
    
solution(s="((()(")