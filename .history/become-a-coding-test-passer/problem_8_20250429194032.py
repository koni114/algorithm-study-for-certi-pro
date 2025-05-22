
def solution(s):
    from collections import deque
    d = deque([])
    for chr in s:
        if chr == "(":
            d.append(chr)
        else:
            if len(d) < 1:
                return False
            d.pop()
    
    if len(d) > 1:
        return False
    return True
    
    
solution(s="((()))(")