def solution(n, k, cmd):
    from collections import deque
    remove_row = deque([])
    check = ['O' for _ in range(n)]
    
    for cur_cmd in cmd:
        cur_cmd_list = cur_cmd.split(" ")
        
        cur_str = cur_cmd_list[0]
        
        if cur_str == "D":
            k = k + int(cur_cmd_list[1])
            k = k if k <= n - 1 else n - 1
        elif cur_str == "U":
            k = k - int(cur_cmd_list[1])
            
    
    
    
    answer = ''
    return answer
    
    
    