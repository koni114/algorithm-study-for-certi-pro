def solution(n, k, cmd):
    from collections import deque
    rm_stack = deque([])
    
    up_list = [range(-1, n)]
    
    answer = ''
    return answer