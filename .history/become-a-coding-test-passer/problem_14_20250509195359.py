def solution(n, k, cmd):
    from collections import deque
    d_left, d_right, d_rm = deque([i for i in range(k)]), deque([i for i in range(n-1, k)]), deque([])
    
    for cur_cmd in cmd:
        cur_cmd_list = cur_cmd.split(" ")
        cursor = cur_cmd_list[0]
        if cursor == "D":
            dir_v = int(cur_cmd_list[0])

    
    
    
    answer = ''
    return answer
    
    
    