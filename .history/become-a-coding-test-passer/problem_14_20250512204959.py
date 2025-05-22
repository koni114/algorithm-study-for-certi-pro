def solution(n, k, cmd):
    from collections import deque
    rm_stack = deque([])
    
    up_list = [range(n+1)]
    
    answer = ''
    return answer