
def solution(s="(())()"):
    from collections import deque
    d = deque([])
    for chr in s:
        if chr == "(":
            d.append(chr)
    